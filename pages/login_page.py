import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")

    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.login_button)

    def login_error(self):
        self.verify_exist_element(self.error_message_login)

    def verify_text_message(self, text):
        find_text = self.get_text(self.error_message_login)
        assert find_text == text, (f"O texto retornado foi '{find_text}', mas era esperado o "
                                   f"texto '{text}'")
