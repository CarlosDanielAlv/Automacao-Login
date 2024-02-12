import pytest
import conftest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.realizar_compra
class TestCT03:
        def test_realizar_compra(self):
                driver = conftest.driver
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

                driver.find_element(By.ID, 'checkout').click()
                driver.find_element(By.ID, 'first-name').send_keys('Carlos')
                driver.find_element(By.ID, 'last-name').send_keys('Daniel')
                driver.find_element(By.ID, 'postal-code').send_keys('0000-000')
                driver.find_element(By.ID, 'continue').click()

                assert (driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Backpack"]')
                        .is_displayed())
                assert (driver.find_element(By.XPATH, '//div[@class="inventory_item_name" and text()="Sauce Labs Bike Light"]')
                        .is_displayed())


                driver.find_element(By.ID, 'finish').click()
                assert driver.find_element(By.XPATH, '//h2[@class="complete-header"]').text == 'Thank you for your order!'
                print("Compra finalizada com sucesso")
