import pytest
import pytest_check as check
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
#from data.users import USERS
#from data.checkout_data import usuarios_checkout
from utils.helpers import load_user_csv, load_user_json

load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")


@pytest.mark.parametrize("username, password", load_json)
#@pytest.mark.parametrize("checkout_data", usuarios_checkout)

#declaro mi test
def test_checkout_saucedemo(driver,username, password):
    login_page = LoginPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)


    login_page.open()
    login_page.login(username,password)


    cart_page.add_product()
    print("Después de agregar:", driver.current_url)
    cart_page.open_cart()
    print("Después de ir al carrito:", driver.current_url)
    checkout_page.init_cart()
    #assert"cart.html" in driver.current_url
    checkout_page.complete_form()
   
    checkout_page.continuar()
    checkout_page.finish()

    mensaje = checkout_page.mensaje_exito()

    check.equal(
        mensaje,
        "Thank you for your order!",
        "NO SE COMPLETÓ LA COMPRA"
    )
    
    


