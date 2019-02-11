from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class Searchitem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/HAIER/Desktop/selenium-java/chromedriver.exe")
        cls.driver.get("http://127.0.0.1:8000")
        cls.driver.maximize_window()

    def test_search_item(self):
        search_bar = self.driver.find_element_by_xpath("//*[@id='navbar']/ul[1]/form/div/input")
        search_bar.send_keys("shirt")
        search_bar.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//*[@id='img']").click()
        heading = self.driver.find_element_by_tag_name('h2')
        self.assertEqual("Blue shirt", heading.text)

    @classmethod
    def tearDown(cls):
        cls.driver.close()



if __name__ == '__main__':
    unittest.main()


