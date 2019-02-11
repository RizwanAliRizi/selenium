from selenium import webdriver
from set_driver import set_driver
from selenium.webdriver.common.keys import Keys
import unittest

class AddToCartTest(unittest.TestCase):
    # driver = webdriver.Chrome()
    def setUp(self):
        self.driver = set_driver()
    def tearDown(self):
        self.driver.quit()


    def test_add_product_to_cart(self):
        # self.setUp()
        #driver = webdriver.Chrome(executable_path=r"C:\Users\Muhammad Salman\Downloads\Compressed\chromedriver.exe")
        self.driver.get("http://localhost:8000/products")

        assert "eCommerce" in self.driver.title

        gotoProduct = self.driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/h4/a')
        gotoProduct.click()

        quantity = self.driver.find_element_by_xpath('//*[@id="add-form"]/input[2]')
        quantity.clear()
        quantity.send_keys("2")
        addButton = self.driver.find_element_by_id("submit-btn")
        addButton.click()
        assert "Successfully added to the cart" not in self.driver.page_source
        self.driver.quit()
        # self.tearDown()
