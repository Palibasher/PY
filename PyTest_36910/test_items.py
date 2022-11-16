import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//"


def test_item_page_contain_add_button(browser):
    browser.get(link)
    wait10 = WebDriverWait(browser, 10, 0.1)
    #Создаем список из наших кнопок, если длина больше 0, значит кнопка есть.
    assert len(wait10.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")))) > 0, "Ошибка, кнопка пропала!"
    time.sleep(30)