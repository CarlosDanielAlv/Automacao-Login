import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.adicionar_produtos_carrinho
class TestCT01:
        def test_ct01_adicionar_produtos_carrinho(self):
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
