from selenium import webdriver
import unittest
from time import sleep
import threading

browser_list = ['chrome', 'firefox']
class SelectCategoryMulti(unittest.TestCase):

    thread_list = []
    driver_list = []

    def setUp(self):
        for browser in browser_list:
            if browser is 'chrome':
                self.driver = webdriver.Chrome(executable_path="C:/Users/HAIER/Desktop/selenium-java/chromedriver.exe")
                thread = threading.Thread(target=self.select_category, args=(self.driver, "chrome_category"), name="Thread1")
                self.thread_list.append(thread)
                self.driver_list.append(self.driver)
            elif browser is 'firefox':
                self.driver = webdriver.Firefox(executable_path="C:/Users/HAIER/Downloads/geckodriver-v0.23.0-win64/geckodriver.exe")
                thread = threading.Thread(target=self.select_category, args=(self.driver, 'firefox_category'), name='Thread2')
                self.thread_list.append(thread)
                self.driver_list.append(self.driver)

    def test_selectcategory(self):
        for thread in self.thread_list:
            thread.start()
            sleep(5)

    def select_category(self, driver, category_name):

        self.driver.get("http://127.0.0.1:8000")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//*[@id='navbar']/ul[1]/li[3]/a").click()
        select_shirt = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/h4/a')
        sleep(3)
        select_shirt.click()
        sleep(5)
        self.assertIn("eCommerce", self.driver.title)

    def tearDown(self):
        for thread in self.thread_list:
            thread.join()

        for driver in self.driver_list:
            driver.close()



if __name__ == '__main__':
    unittest.main()


