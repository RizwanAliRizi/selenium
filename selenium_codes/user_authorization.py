from admin_login import admin_login
import unittest
from time import sleep


class user_authentication(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()


    def test_user_authorize(self):
        users = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[1]/tbody/tr[2]/th/a')
        users.click()

        select_user = self.driver.find_element_by_xpath("//*[@id='result_list']/tbody/tr[1]/th/a")
        select_user.click()

        self.driver.find_element_by_id("id_is_active").click()

        save_button = self.driver.find_element_by_xpath('//*[@id="user_form"]/div[3]/div[2]/input[3]')
        save_button.click()
        sleep(2)
        self.assertIn('Select user to change | Django site admin', self.driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
