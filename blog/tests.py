from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class BlogATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        # username, password, and driver
        user = 'instructor'
        pwd = 'maverick1a'
        driver = self.driver

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/admin')

        elem = driver.find_element_by_id('id_username')
        elem.send_keys(user)
        elem = driver.find_element_by_id('id_password')
        elem.send_keys(pwd)
        time.sleep(30)
        elem.send_keys(Keys.RETURN)
        driver.get('http://127.0.0.1:8000')
        assert 'Logged In'
        time.sleep(10)

        # find Add button
        driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
        time.sleep(10)

        elem = driver.find_element_by_id("id_title")
        elem.send_keys("This is the last test post with selenium")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This is the last test post of text with selenium")
        time.sleep(30)

        # find Save button
        driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(30)
        assert "Posted Blog Entry"
        driver.get("http://127.0.0.1:8000")
        time.sleep(30)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
