import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.carrinho_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.adicionar_produtos_carrinho
class TestCT01:
        def test_ct01_adicionar_produtos_carrinho(self):
                login_page = LoginPage()
                home_page = HomePage()
                cart_page = CartPage()

                login_page.login('standard_user', 'secret_sauce')
                home_page.verify_login_success()

                # Adicionar mochila ao carrinho
                home_page.add_cart("Sauce Labs Backpack")
                # Acessar carrtinho
                home_page.cart_access()
                # Verificar se mochila foi adicionada
                cart_page.verify_cart_product("Sauce Labs Backpack")
                # Clicar para voltar tela de produtos
                cart_page.continue_buy()

                # Adicionar mochila ao carrinho
                home_page.add_cart("Sauce Labs Bike Light")
                # Acessar carrtinho
                home_page.cart_access()
                # Verificar se mochila foi adicionada
                cart_page.verify_cart_product("Sauce Labs Bike Light")
                # Clicar para voltar tela de produtos
                cart_page.continue_buy()
