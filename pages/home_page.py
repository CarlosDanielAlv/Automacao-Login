from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.page_title = (By.XPATH, '//span[@class="title"]')
        self.inventory_item = (By.XPATH, '//div[@class="inventory_item_name " and text()="{}"]')
        self.cart_button = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]')
        self.cart_icon = (By.XPATH, '//*[@class="shopping_cart_link"]')

    def verify_login_success(self):
        self.verify_exist_element(self.page_title)

    def add_cart(self, item_name):
        item = (self.inventory_item[0], self.inventory_item[1].format(item_name))
        self.click(item)
        self.click(self.cart_button)

    def cart_access(self):
        self.click(self.cart_icon)

