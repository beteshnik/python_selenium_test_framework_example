# -*- coding: utf-8 -*-
#Шаблон теста
import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTemplate(unittest.TestCase):
    #Определяем окружение из переданных параметров: адрес грида для тестов, адрес тестовой площадки, браузер
    if len(sys.argv) < 4:
        print('Не задано окружение: адрес грида для тестов, адрес тестовой площадки, браузер')
        sys.exit(1)
    grid_url = sys.argv[1]
    target_url = sys.argv[2]
    browser = sys.argv[3]
    def setUp(self):
        #Запуск драйвера
        if self.browser == 'FIREFOX':
            self.driver = webdriver.Remote(command_executor=self.grid_url, desired_capabilities=DesiredCapabilities.FIREFOX)
        elif self.browser == 'CHROME':
            self.driver = webdriver.Remote(command_executor=self.grid_url, desired_capabilities=DesiredCapabilities.CHROME)
        else:
            print('Не задан браузер для теста - FIREFOX или CHROME')
            sys.exit(1)			
        self.driver.implicitly_wait(10)

    def tearDown(self):
        #Закрыть драйвер
        self.driver.quit()