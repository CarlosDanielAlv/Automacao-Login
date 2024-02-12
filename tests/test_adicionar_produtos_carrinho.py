import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

driver.find_element(By.ID, 'user-name').send_keys('standard_user')
driver.find_element(By.ID, 'password').send_keys('secret_sauce')
driver.find_element(By.ID, 'login-button').click()
assert driver.find_element(By.XPATH, '//span[@class="title"]').is_displayed()

driver.find_element(By.XPATH, '//div[@class="inventory_item_name " and text()="Sauce Labs Backpack"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]').click()
driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]').click()
assert (driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
        .is_displayed())

driver.find_element(By.ID, 'continue-shopping').click()
driver.find_element(By.XPATH, '//div[@class="inventory_item_name " and text()="Sauce Labs Bike Light"]').click()
driver.find_element(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]').click()
driver.find_element(By.XPATH, '//*[@class="shopping_cart_link"]').click()
assert (driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]')
        .is_displayed())


time.sleep(4)
