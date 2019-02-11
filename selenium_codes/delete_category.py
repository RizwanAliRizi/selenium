import os
from admin_login import admin_login
import unittest


class DeleteCategoryTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def test_delete_category(self):

        view_categories = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[1]/th/a')
        view_categories.click()


        select_category = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td/input')
        select_category.click()

        self.driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/div/select/option[2]').click()

        delete_button = self.driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/div/button')
        delete_button.click()

        delete_sure_button = self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/div/input')
        delete_sure_button.click()

        self.assertIn('Select category', self.driver.title)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')