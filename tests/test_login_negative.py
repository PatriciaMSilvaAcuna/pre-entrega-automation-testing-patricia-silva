import pytest_check as check
import pytest
from pages.login_page import LoginPage
from utils.logger import logger
from utils.helpers import load_user_json

invalid_users = load_user_json("data/invalid_users.json")


@pytest.mark.parametrize("username,password", invalid_users)
def test_login_negative(driver, username, password):

    logger.info("=" * 60)
    logger.info("INICIANDO TEST: LOGIN INVÁLIDO")
    logger.info("=" * 60)

    login_page = LoginPage(driver)

    login_page.open()

    login_page.login(username,password)

    mensaje = login_page.obtener_error()
    

    print("MENSAJE:", mensaje)
    logger.info("VALIDANDO MENSAJE DE ERROR")
    check.equal(
        mensaje,
        "Epic sadface: Username and password do not match any user in this service",
        "NO SE MOSTRÓ EL MENSAJE DE ERROR ESPERADO"
    )

    logger.info("TEST FINALIZADO CORRECTAMENTE")