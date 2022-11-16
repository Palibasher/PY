from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#
#
# def test_this():
#
#     try:
#         link = "https://suninjuly.github.io/math.html"
#         browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#         browser.get(link)
#
#         x = browser.find_element(By.CSS_SELECTOR, ".nowrap[id='input_value']")
#         x_1 = str(math.log(abs(12 * math.sin(int(x.text)))))
#         field = browser.find_element(By.ID, "answer").send_keys(x_1)
#         rob_check = browser.find_element(By.ID, "robotCheckbox").click()
#         rob_rad = browser.find_element(By.ID, "robotsRule").click()
#         submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
#
#
#     finally:
#         time.sleep(5)
#         browser.quit()
#
#
# def test_this():
#
#     try:
#         link = "http://suninjuly.github.io/get_attribute.html"
#         browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#         browser.get(link)
#
#         chest_val = browser.find_element(By.ID, "treasure")
#         chest_val = str(math.log(abs(12 * math.sin(int(chest_val.get_attribute("valuex"))))))
#         field = browser.find_element(By.ID, "answer").send_keys(chest_val)
#         rob_check = browser.find_element(By.ID, "robotCheckbox").click()
#         rob_rad = browser.find_element(By.ID, "robotsRule").click()
#         submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
#
#
#     finally:
#         time.sleep(5)
#         browser.quit()
# def test_this():
#
#     try:
#         link = "https://suninjuly.github.io/selects1.html"
#         browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#         browser.get(link)
#
#         num1 = browser.find_element(By.ID, "num1")
#         num2 = browser.find_element(By.ID, "num2")
#         operation = int(num1.text) + int(num2.text)
#         drop = Select(browser.find_element(By.ID, "dropdown"))
#         drop.select_by_value(str(operation))
#         submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
#
#
#     finally:
#         time.sleep(5)
#         browser.quit()
# test_this()
# browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()

##js
# def test_this():
#
#     try:
#         link = "http://suninjuly.github.io/execute_script.html"
#         browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#         browser.get(link)
#
#         x = browser.find_element(By.ID, "input_value")
#         x_1 = str(math.log(abs(12 * math.sin(int(x.text)))))
#         field = browser.find_element(By.ID, "answer").send_keys(x_1)
#         rob_check = browser.find_element(By.ID, "robotCheckbox").click()
#         button = browser.find_element(By.TAG_NAME, "button")
#         browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#         rob_rad = browser.find_element(By.ID, "robotsRule").click()
#         button.click()
#
#
#     finally:
#         time.sleep(5)
#         browser.quit()
# test_this()

##file
# link = "http://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
# browser.get(link)
# browser.find_element(By.NAME, "firstname").send_keys("Vasya")
# browser.find_element(By.NAME, "lastname").send_keys("Vasya")
# browser.find_element(By.NAME, "email").send_keys("Vasya@f.ru")
# current_dir = os.path.abspath(os.path.abspath('1.txt'))
# browser.find_element(By.ID, "file").send_keys(current_dir)
# browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# js alerts handling
# link = "http://suninjuly.github.io/alert_accept.html"
# browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
# browser.get(link)
# browser.find_element(By.CSS_SELECTOR, "button").click()
# time.sleep(3)
# alert = browser.switch_to.alert
# alert.accept()
# x = browser.find_element(By.ID, "input_value")
# x_1 = str(math.log(abs(12 * math.sin(int(x.text)))))
# field = browser.find_element(By.ID, "answer").send_keys(x_1)
# browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

#js + many windows
# link = "http://suninjuly.github.io/redirect_accept.html"
# browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
# browser.get(link)
# browser.find_element(By.CSS_SELECTOR, "button").click()
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# x = browser.find_element(By.ID, "input_value")
# x_1 = str(math.log(abs(12 * math.sin(int(x.text)))))
# field = browser.find_element(By.ID, "answer").send_keys(x_1)
# browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

#ожидания
# def test_1():
#
#     browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#     browser.implicitly_wait(3)
#     browser.get("http://suninjuly.github.io/wait1.html")
#     button = browser.find_element(By.ID, "verify")
#
#     button.click()
#
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text
# def test_1():
#     browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
#     browser.get("http://suninjuly.github.io/wait2.html")
#     button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
#
#     button = browser.find_element(By.ID, "verify")
#     button.click()
#     message = browser.find_element(By.ID, "verify_message")
#
#     assert "successful" in message.text

browser = webdriver.Chrome(executable_path="C:\\PY\\driver\\cd.exe")
browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button1 = browser.find_element(By.ID, "book").click()
x = browser.find_element(By.ID, "input_value")
_ = x.location_once_scrolled_into_view
x_1 = str(math.log(abs(12 * math.sin(int(x.text)))))
field = browser.find_element(By.ID, "answer").send_keys(x_1)
browser.find_element(By.ID, "solve").click()

