from pages.login_page import LoginPage
from data.users import USERS
from utils.helpers import load_user_csv,load_user_json
import pytest
from faker import Faker


#lo guardo en una variable
#recibe la ubicacion donde esta el archivo
load_csv = load_user_csv("data/users.csv")
load_json = load_user_json("data/users.json")

#instanciamos faker

fake = Faker()


@pytest.mark.parametrize("username, password", load_json)
# declaro el test

def test_login(driver, username, password):
    #instancio mi clase para poder utilizar mis funciones
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)
    
    print("Logueo Exitoso")
    

    name = fake.name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    codigo_postal = fake.postalcode()

    print("DATOS GENERADOs POR FAKER",name,first_name,last_name,email,codigo_postal)

#@pytest.mark.parametrize("i",range(3))
#def test_login_usuario_invalido(driver,i):
 #   login_page = LoginPage(driver)


 #   fake_username = fake.user_name()
 #   fake_password = fake.password()
    


  #  login_page.open()
   # login_page.login(fake_username, fake_password)

    #busca en toda la pagina una palabra dada
   # assert "Epic sadface" in login_page.obtener_error()