import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as crome_options

@pytest.fixture
def get_chrome_options():
    options_c = crome_options()

    options_c.add_argument('chrome')
    options_c.add_argument('--start-maximized')
    options_c.add_argument('--window-size=1900,1200')
    return options_c

@pytest.fixture
def get_webdriver(get_chrome_options):
    options_c = get_chrome_options
    driver = webdriver.Chrome(options=options_c, executable_path="C:\\PY\\driver\\cd.exe")
    return driver

@pytest.fixture(scope="function", autouse=True)
def setup(request, get_webdriver):
    driver = get_webdriver
    # bace_url = "https://coinmarketcap.com/"
    bace_url = "http://petfriends.skillfactory.ru/login"
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(bace_url)
    yield driver
    driver.quit()