import os
from admin_login import admin_login
import unittest


class AddProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def tearDown(self):
        self.driver.quit()

    def test_add_product(self):
        add = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[4]/th/div/a[1]')
        add.click()

        title = self.driver.find_element_by_id('id_title')
        title.send_keys('Blue shirt')

        description = self.driver.find_element_by_id('id_description')
        description.send_keys('Adding product through selenium')

        price = self.driver.find_element_by_id('id_price')
        price.send_keys(int('34'))

        self.driver.find_element_by_xpath('//*[@id="id_default"]/option[text()="Shirts"]').click()

        show_image = self.driver.find_element_by_link_text('Add another Product image')
        show_image.click()

        self.driver.find_element_by_id('id_productimage_set-0-image').send_keys(os.getcwd()+"/products_images"+"/shirt1.jpg")

        save = self.driver.find_element_by_xpath('//*[@id="product_form"]/div[3]/div[2]/input[3]')
        save.click()

        # She notices the page title and header mention to-do lists
        self.assertIn('Select product', self.driver.title)
        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')