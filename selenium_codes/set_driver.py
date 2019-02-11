from selenium import webdriver


def set_driver():
    driver = webdriver.Chrome("C:\\Users\\ehtis_000\\Downloads\\Compressed\\chromedriver.exe")
    driver.maximize_window()
    return driver
