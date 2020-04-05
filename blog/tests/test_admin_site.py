from django.test import TestCase
from selenium import webdriver
import unittest


print(unittest)


class TestAdminSite(unittest.Testcase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Edge()
        user = 'instructor'
        pwd = 'maverick1a'

        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1:8000/admin')

    def test_login(self):
        driver = self.driver
        # placeholder

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
