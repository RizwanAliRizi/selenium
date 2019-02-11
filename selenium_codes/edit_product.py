from admin_login import admin_login
import unittest


class EditProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def tearDown(self):
        self.driver.quit()

    def test_edit_product(self):

        edit = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[4]/th/a[text() = "Products"]')
        edit.click()

        # first_product = self.driver.find_element_by_link_text('First')
        first_product = self.driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[9]/th/a')
        first_product.click()

        title = self.driver.find_element_by_id('id_title')
        title.send_keys('first shirt')

        sale = self.driver.find_element_by_id('id_variation_set-0-sale_price')
        sale.send_keys(int('10'))

        save = self.driver.find_element_by_xpath('//*[@id="product_form"]/div[3]/div[2]/input[3]')
        save.click()

        # She notices the page title and header mention to-do lists
        self.assertIn('Select product', self.driver.title)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
