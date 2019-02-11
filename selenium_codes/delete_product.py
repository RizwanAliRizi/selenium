from admin_login import admin_login
import unittest


class DeleteProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def tearDown(self):
        self.driver.quit()

    def test_delete_product(self):
        view_products = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[4]/th/a[text() = "Products"]')
        view_products.click()

        select_product = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[1]/td[1]/input')
        select_product.click()

        self.driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/div/select/option[2]').click()

        delete_button = self.driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/div/button')
        delete_button.click()

        delete_sure_button = self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/div/input')
        delete_sure_button.click()

        # She notices the page title and header mention to-do lists
        self.assertIn('Select product', self.driver.title)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')