import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT01:
    def test_login_valido(self):
        login_page = LoginPage()
        home_page = HomePage()

        login_page.login('standard_user', 'secret_sauce')
        home_page.verify_login_success()
