import os
from admin_login import admin_login
import unittest


class AddProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def tearDown(self):
        self.driver.quit()
		

    def test_add_user(self):
        # driver = webdriver.Chrome(executable_path=r"C:\Users\Muhammad Salman\Downloads\Compressed\chromedriver.exe")
        add_user = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[1]/tbody/tr[2]/th/div/a[1]')
        add_user.click()

        usernameField = self.driver.find_element_by_id("id_username")
        passwordField = self.driver.find_element_by_id('id_password1')
        confirmPasswordField = self.driver.find_element_by_id('id_password2')

        
		usernameField.send_keys("salman1")
		passwordField.send_keys("12345678")
		confirmPasswordField.send_keys("12345678")

        save = self.driver.find_element_by_xpath('//*[@id="user_form"]/div[3]/div[2]/input[1]')

        save.click()
		
		sleep(10)

        # self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')