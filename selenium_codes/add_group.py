import unittest
from selenium import webdriver
from admin_login import admin_login
from time import sleep

class AddCategoryTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def test_add_group(self):
        add_group = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[1]/tbody/tr[1]/th/a')
        add_group.click()

        self.driver.find_element_by_xpath('//*[@id="content-navbar-collapse"]/ul/li/a').click()

        title = self.driver.find_element_by_id("id_name")
        title.send_keys("Group_chrome")

        self.driver.find_element_by_xpath('//*[@id="id_permissions_add_all_link"]').click()

        self.driver.find_element_by_xpath("//input[@name='_save']").click()

        self.assertIn('group', self.driver.title)
        sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
