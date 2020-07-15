# -*- coding: utf-8 -*-
#Часто используемые функции

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui

#Проверка наличия элемента с перехватом исключения в случае, когда элемент отсутствует
def element_present(driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True

#Ждём, когда элемент станет видимым. В дополнение к implicit ожиданию для особых случаев
def wait_element(driver, how, what, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((how, what)))
        return True
    except TimeoutException:
        return False

#Ждём, когда страница загрузится (загрузится DOM)
def wait_page(driver, timeout=15):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'