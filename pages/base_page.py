import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()

    def verify_exist_element(self, locator):
        assert self.find_element(locator).is_displayed(), f'O Elemento "{locator}" não foi encontrado, na tela'

    def get_text(self, locator):
        self.wait_show_element(locator)
        return self.find_element(locator).text

    def wait_show_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))

    def verify_element_exist(self, locator):
        assert self.find_element(locator), f'O Elemento "{locator}" não existe, mas é esperado que exista'

    def verify_element_not_exist(self, locator):
        assert len(self.find_elements(locator)) == 0, f'O Elemento "{locator}" existe, mas é esperado que não exista'

    def double_click(self, locator):
        element = self.wait_show_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def context_click(self, locator):
        element = self.wait_show_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    def key_press(self, locator, key):
        element = self.wait_show_element(locator)
        if key == "ENTER":
            element.send_keys(Keys.ENTER)
