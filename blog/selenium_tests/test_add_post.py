import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class TestAddPost(unittest.TestCase):
    """
    placeholder
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge('C:\\Users\\JordonTrujillo\\Documents\\temp\\web-application-' +
                                    'development-isqa-3900\\edgedriver_win64\\msedgedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get('http://127.0.0.1:8000/')

    def test_post(self):
        """
        placeholder
        :return:
        """
        # driver = self.driver
        self.driver.find_element_by_xpath('/html/body/div[1]/a/span').click()
        elem = self.driver.find_element_by_id('id_title')
        elem.send_keys('Test Selenium Post Title')
        elem = self.driver.find_element_by_id('id_text')
        elem.send_keys('Test Selenium Post Text')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button').click()
        time.sleep(4)

        self.assertTrue(self.driver.find_element_by_class_name('post'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
