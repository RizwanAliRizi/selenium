import unittest
from selenium import webdriver
from admin_login import admin_login
from selenium.webdriver.common.keys import Keys


class EditCategoryTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def test_edit_category(self):
        edit = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[1]/th/div/a[2]')
        edit.click()


        first_category = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/th/a')
        first_category.click()

        title = self.driver.find_element_by_id("id_title")
        title.clear()
        title.send_keys("Ties")

        slug = self.driver.find_element_by_id("id_slug")
        slug.clear()
        slug.send_keys("Ties")

        description = self.driver.find_element_by_id("id_description")
        description.clear()
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
