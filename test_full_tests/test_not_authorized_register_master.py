# -*- coding: utf-8 -*-
import unittest
import selenium
from selenium.webdriver.common.by import By
from test_utils import test_utils
from test_utils import test_template

class NotAuthorisedRegisterMaster(test_template.TestTemplate):
    """Кнопка/ссылка регистрации анкеты мастера для неавторизованного пользователя.
    Пользовательская история: https://gitlab.digillect.com/my-salon/home/issues/2.
    Неавторизованный пользователь заходит на сайт.
    """
    
    def test_not_authorised_register_master(self):
        """Начальные условия: пользователь не авторизован.
        """
        browser=self.driver
        url=self.target_url
        """Действие: открыть сайт.
        """
        browser.get(url)
        """Проверка: открыта страница для неавторизованного пользователя.
        """
        """Проверка: есть кнопка/ссылка регистрации анкеты мастера.
        """
        xpath = "//*[text()='Google']";
        message = "Проверка: есть кнопка/ссылка регистрации анкеты мастера.\n" + self.__doc__
        self.assertTrue(test_utils.element_present(browser, By.XPATH, xpath), message)
        """Действие: кликнуть кнопку/ссылку регистрации анкеты мастера.
        """
        """Проверка: открыта страница для регистрации анкеты мастера.
        """