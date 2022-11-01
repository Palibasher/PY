import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



pytest.mark.usefixtures("setup")
class Test_Pet_bros:
    """Класс для тестирования сайта PetFriends. Драйвер настраивается в фикстурах и передается из них в переменной"""
    def test_show_my_pets(self, setup):
        test_driver = setup
        test_driver.implicitly_wait(10)
        # Вводим email
        test_driver.find_element("id", "email").send_keys('vasya@mail.com')
        # Вводим пароль
        test_driver.find_element("id", "pass").send_keys('12345')
        # Нажимаем на кнопку входа в аккаунт
        test_driver.find_element("css selector", 'button[type="submit"]').click()
        # Проверяем, что мы оказались на главной странице пользователя
        assert test_driver.find_element(By.TAG_NAME, "h1").text == "PetFriends"

    def test_sf_25_3(self, setup):
        """ Тесть проверяет, что:
            1. Присутствуют все питомцы.
            2. Хотя бы у половины питомцев есть фото.
            3. У всех питомцев есть имя, возраст и порода.
            4. У всех питомцев разные имена.
            5. В списке нет повторяющихся питомцев."""
        test_driver = setup
        test_driver.find_element("id", "email").send_keys('vasya1@mail.com')
        # Вводим пароль
        test_driver.find_element("id", "pass").send_keys('12345')
        # Нажимаем на кнопку входа в аккаунт
        test_driver.find_element("css selector", 'button[type="submit"]').click()
        test_driver.find_element("css selector", '.nav-link').click()

        images = test_driver.find_elements("css selector", 'table.table-hover tbody tr th img')
        names = test_driver.find_elements("css selector", 'table.table-hover tbody tr td:nth-child(2)')
        descriptions = test_driver.find_elements("css selector", 'table.table-hover tbody tr td:nth-child(3)')
        ages = test_driver.find_elements("css selector", 'table.table-hover tbody tr td:nth-child(4)')
        ##Вытаскиваем кол-во питомцев для сравнения со счетчиком
        user_info_block = test_driver.find_element("xpath", '/html/body/div[1]/div/div[1]').text
        str_limiter = user_info_block.find("Д")
        my_pet_number = [i for i in user_info_block[0:str_limiter:] if i.isdigit()]
        int(my_pet_number := int(my_pet_number := "".join(map(str, my_pet_number))))
        ##считаем питомцев с фото
        image_counter = 0
        for i in range(len(images)):
            if images[i].get_attribute('src') != None:
                image_counter += 1
        ##создаем общий список (имя + описание + возраст)
        pets_descrip = [i.text for i in descriptions] ##создаем список описаний
        pets_ages = [i.text for i in ages] ##возрастов
        pets_names = [i.text for i in names] ##имен
        pets_data = [pets_descrip[i] + " " + pets_names[i] + " " + pets_ages[i] for i in range(len(names))] ##описание + имя + возраст
        dup = [i for i in pets_data if pets_data.count(i) > 1] ##если есть дупликаты, то создаем список из них

        assert my_pet_number == len(images) ##кол-во питомцев совпадает со счетчиком
        assert my_pet_number/2 <= image_counter ##Хотя бы у половины питомцев есть фото.
        assert int((len(ages) + len(names) + len(descriptions))/3) == my_pet_number ##У всех питомцев есть имя, возраст и порода.
        assert len([i for i in pets_data if pets_data.count(i) > 1]) == 0 ##Список дупликатов пустой
        assert len([i for i in pets_names if pets_names.count(i) > 1]) == 0 ##У всех питомцев разные имена.

    def test_sf_25_5_Wait_and_EC(self, setup):
        """Тест повторяет предыдущий, но использует WebDriverWait и expected_conditions"""
        test_driver = setup
        wait_10 = WebDriverWait(test_driver, 10, 0.2) ##создаем переменную для ожидания в макс 10с
        ##ожидаем элемент для ввода текста и когда ожидаемые кондиции наступают, отправляем текст
        wait_10.until(expected_conditions.presence_of_element_located((By.ID, "email"))).send_keys('vasya1@mail.com')
        wait_10.until(expected_conditions.presence_of_element_located((By.ID, "pass"))).send_keys('12345')

        wait_10.until(expected_conditions.presence_of_element_located(("css selector", 'button[type="submit"]'))).click()
        wait_10.until(expected_conditions.presence_of_element_located(("css selector", '.nav-link'))).click()

        images = test_driver.find_elements("css selector", 'table.table-hover tbody tr th img')
        names = wait_10.until(expected_conditions.visibility_of_all_elements_located(("css selector", 'table.table-hover tbody tr td:nth-child(2)')))
        descriptions = wait_10.until(expected_conditions.visibility_of_all_elements_located(("css selector", 'table.table-hover tbody tr td:nth-child(3)')))
        ages = wait_10.until(expected_conditions.visibility_of_all_elements_located(("css selector", 'table.table-hover tbody tr td:nth-child(4)')))

        user_info_block = test_driver.find_element("xpath", '/html/body/div[1]/div/div[1]').text
        str_limiter = user_info_block.find("Д")
        my_pet_number = [i for i in user_info_block[0:str_limiter:] if i.isdigit()]
        int(my_pet_number := int(my_pet_number := "".join(map(str, my_pet_number))))

        image_counter = 0
        for i in range(len(images)):
            if images[i].get_attribute('src') != None:
                image_counter += 1

        pets_descrip = [i.text for i in descriptions]
        pets_ages = [i.text for i in ages]
        pets_names = [i.text for i in names]
        pets_data = [pets_descrip[i] + " " + pets_names[i] + " " + pets_ages[i] for i in range(len(names))]
        dup = [i for i in pets_data if pets_data.count(i) > 1]

        assert my_pet_number == len(images) ##кол-во питомцев совпадает со счетчиком
        assert my_pet_number/2 <= image_counter ##Хотя бы у половины питомцев есть фото.
        assert int((len(ages) + len(names) + len(descriptions))/3) == my_pet_number ##У всех питомцев есть имя, возраст и порода.
        assert len([i for i in pets_data if pets_data.count(i) > 1]) == 0 ##Список дупликатов пустой
        assert len([i for i in pets_names if pets_names.count(i) > 1]) == 0 ##У всех питомцев разные имена.


