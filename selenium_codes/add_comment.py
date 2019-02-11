from set_driver import set_driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AddCommentTest(unittest.TestCase):
    def setUp(self):
        self.driver = set_driver()

    def tearDown(self):
        self.driver.quit()

    def test_add_product_to_cart(self):
        self.driver.get("http://127.0.0.1:8000/products/12/")
        assert "eCommerce" in self.driver.title
        gotoProduct = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/h4/a')
        gotoProduct.click()

        sleep(5)

        self.driver.find_element_by_id("hcb_form_content").send_keys("First comment")

        self.driver.find_element_by_id("hcb_submit").click()


if __name__ == "__main__":
    unittest.main(warnings='ignore')
