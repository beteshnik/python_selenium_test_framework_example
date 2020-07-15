# -*- coding: utf-8 -*-
#Полный набор тестов
import sys
import unittest
from unittest import TextTestRunner
import xmlrunner


suite = unittest.TestLoader().discover('test_full_tests')

if __name__ == '__main__':
    output = open('results.xml', 'wb')
    result = xmlrunner.XMLTestRunner(output).run(suite)
    if not result.wasSuccessful():
        print('Есть упавшие тесты')
        sys.exit(1)