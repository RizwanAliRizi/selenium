import unittest
from selenium import webdriver
from time import sleep
import threading

param_list = ['chrome', 'firefox']


class MultibrowserTest(unittest.TestCase):
    drivers_list = []
    threads_list = []

    def setUp(self):
        for d in param_list:
            if d is "chrome":
                driver = webdriver.Chrome("C:\\Users\\ehtis_000\\Downloads\\Compressed\\chromedriver.exe")
                t = threading.Thread(target=self.add_category, args=(driver, "chrome_category"), name="Thread1")
                self.threads_list.append(t)
                self.drivers_list.append(driver)
            elif d is "firefox":
                driver = webdriver.Firefox()
                t = threading.Thread(target=self.add_category, args=(driver, "firefox_category"), name="Thread2")
                self.threads_list.append(t)
                self.drivers_list.append(driver)

    def test_driver(self):
        for t in self.threads_list:
            t.start()
            sleep(4)

    def add_category(self, driver, category_name):
        # Admin login part

        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        name = driver.find_element_by_id("id_username")
        name.send_keys("selenium4")

        password = driver.find_element_by_id("id_password")
        password.send_keys('sqa12345')

        btn = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[3]/input')
        btn.click()

        # Adding Category

        add = driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[1]/th/div/a[1]')
        add.click()

        title = driver.find_element_by_id("id_title")
        title.send_keys(category_name)

        slug = driver.find_element_by_id("id_slug")
        slug.send_keys(category_name)

        description = driver.find_element_by_id("id_description")
        description.send_keys("this product will make you feel better")

        save = driver.find_element_by_xpath('//*[@id="category_form"]/div[3]/div[2]/input[3]')
        save.click()

        self.assertIn('category', driver.title)

    def tearDown(self):
        for t in self.threads_list:
            t.join()

        for d in self.drivers_list:
            d.quit()


if __name__ == '__main__':
    unittest.main()
