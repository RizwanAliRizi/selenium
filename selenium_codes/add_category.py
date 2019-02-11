import unittest
from selenium import webdriver
from admin_login import admin_login
from selenium.webdriver.common.keys import Keys


class AddCategoryTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def test_add_category(self):
        add = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[1]/th/div/a[1]')
        add.click()

        title = self.driver.find_element_by_id("id_title")
        title.send_keys("shoes")

        slug = self.driver.find_element_by_id("id_slug")
        slug.send_keys("shoes")

        description = self.driver.find_element_by_id("id_description")
        description.send_keys("this product will make you feel better")

        #activeCheckbox = self.driver.find_element_by_id("id_active")
       # activeCheckbox.click()


        save = self.driver.find_element_by_name('_save')
        save.click()


        self.assertIn('Select category', self.driver.title)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
