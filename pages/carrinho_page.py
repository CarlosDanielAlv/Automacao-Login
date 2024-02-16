import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.inventory_item = (By.XPATH, '//div[@class="inventory_item_name" and text()="{}"]')
        self.continue_buy_button = (By.ID, 'continue-shopping')

    def verify_cart_product(self, item_name):
        item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
        self.verify_exist_element(item)

    def continue_buy(self):
        self.click(self.continue_buy_button)
