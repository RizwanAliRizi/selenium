import os
import csv
from admin_login import admin_login
import unittest


class AddProductTest(unittest.TestCase):

    def setUp(self):
        self.driver = admin_login()

    def tearDown(self):
        self.driver.quit()

    def test_add_product(self):
        view_products = self.driver.find_element_by_xpath('//*[@id="content-main"]/div/table[5]/tbody/tr[4]/th/a[text() = "Products"]')
        view_products.click()

        with open("product_data/detail.csv") as f:
            contents_of_file = csv.reader(f)
            for each_line in contents_of_file:
                add = self.driver.find_element_by_xpath('//*[@id="content-navbar-collapse"]/ul/li/a')
                add.click()
                title = self.driver.find_element_by_id('id_title')
                title.send_keys(each_line[0])

                description = self.driver.find_element_by_id('id_description')
                description.send_keys(each_line[1])

                price = self.driver.find_element_by_id('id_price')
                price.send_keys(int(each_line[2]))

                self.driver.find_element_by_xpath('//*[@id="id_default"]/option[text()="jeans"]').click()

                show_image = self.driver.find_element_by_link_text('Add another Product image')
                show_image.click()

                self.driver.find_element_by_id('id_productimage_set-0-image').send_keys(
                    os.getcwd() + "\\product_data\\" + each_line[0] + ".jpg")

                save = self.driver.find_element_by_xpath('//*[@id="product_form"]/div[3]/div[2]/input[3]')
                save.click()

                self.assertIn('Select product', self.driver.title)



if __name__ == '__main__':
    unittest.main(warnings='ignore')
