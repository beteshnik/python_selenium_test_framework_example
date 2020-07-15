# -*- coding: utf-8 -*-
import unittest
import selenium
from test_utils import test_template


class NotAuthorisedRegisterMaster(test_template.TestTemplate):
    """Cайт доступен"""
    def test_not_authorised_register_master(self):
        """Начальные условия: нет
        """
        """1. Действие: открыть сайт
        """
        self.driver.get(self.target_url)
        """2. Проверка: открыт сайт
        """
        assert "Google" in self.driver.title