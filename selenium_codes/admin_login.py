from set_driver import set_driver


def admin_login():
    driver = set_driver()
    driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
    name = driver.find_element_by_id("id_username")
    name.send_keys("selenium4")

    password = driver.find_element_by_id("id_password")
    password.send_keys('sqa12345')

    btn = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[3]/input')
    btn.click()
    return driver


# assert "Django" in driver.title

# driver.implicitly_wait(10)



