import pytest
import pytest_check as check

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.helpers import load_user_json
from utils.logger import logger

load_json = load_user_json("data/users.json")


@pytest.mark.parametrize("username, password", load_json)
def test_add_product_to_cart(driver, username, password):

    logger.info("=" * 60)
    logger.info("INICIANDO TEST: AGREGAR PRODUCTO AL CARRITO")
    logger.info("=" * 60)

    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(username, password)

    cart_page.add_product()
    cart_page.open_cart()

    check.equal(
        cart_page.get_cart_badge(),
        "1",
        "EL CARRITO NO CONTIENE UN PRODUCTO"
    )

    check.equal(
        cart_page.get_product_name(),
        "Sauce Labs Backpack",
        "EL PRODUCTO AGREGADO NO ES EL ESPERADO"
    )

    logger.info("TEST FINALIZADO CORRECTAMENTE")


@pytest.mark.parametrize("username, password", load_json)
def test_delete_product_from_cart(driver, username, password):

    logger.info("=" * 60)
    logger.info("INICIANDO TEST: ELIMINAR PRODUCTO DEL CARRITO")
    logger.info("=" * 60)

    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    login_page.open()
    login_page.login(username, password)

    cart_page.add_product()
    cart_page.open_cart()

    cart_page.delete_product()

    check.is_true(
        cart_page.is_cart_empty(),
        "EL CARRITO NO QUEDÓ VACÍO"
    )

    logger.info("TEST FINALIZADO CORRECTAMENTE")