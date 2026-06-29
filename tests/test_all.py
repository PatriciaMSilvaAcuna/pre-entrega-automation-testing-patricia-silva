from api.api_client import get_users, create_user, login_user
import pytest_check as check
from utils.logger import logger

def test_get_user():

    logger.info("---CONSULTANDO LISTA DE USUARIOS---")

    response = get_users()

    

    body = response.json()
    
    check.equal(
         response.status_code,
         200,
         "EL STATUS CODE NO ES 200"

    )
    check.is_in("data", body, "NO EXISTE LA KEY DATA")
    check.is_instance(body["data"], list, "DATA NO ES LISTA")
    

def test_create_user(users_data):
    logger.info("---CREANDO USUARIO---")

    response = create_user(
        users_data["name"],
        users_data["job"]

    )
    body = response.json()

    check.equal(response.status_code,
                 201,
                 "EL STATUS CODE NO ES 201"
                 )
    check.equal(body["name"],
                 users_data["name"],
                 "EL NOMBRE NO COINCIDE")
    check.equal(body["job"],
                 users_data["job"],
                 "EL TRABAJO NO COINCIDE")



def test_login_user():
    logger.info("---LOGIN EXITOSO---")

    response = login_user(
        "eve.holt@reqres.in",
        "cityslicka"
    )
    
    body = response.json()

    check.equal(
        response.status_code,
        200,
        "EL LOGIN FALLÓ"
    )

    
