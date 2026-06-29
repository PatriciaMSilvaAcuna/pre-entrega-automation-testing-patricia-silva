#inicializamos nuestro web driver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# importo los servicios para actualizar el navegador 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import json
import tempfile
# funcion que nos permite instalar el Driver

def get_driver():

    # Configuración de Chrome para automatización
    options = Options()

    # Maximiza la ventana al iniciar.
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    # Perfil temporal de Chrome
    temp_profile = tempfile.mkdtemp()
    options.add_argument(f"--user-data-dir={temp_profile}")
    # Desactiva el aviso de guardar contraseñas.
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }
    )

    # Desactiva notificaciones del navegador.
    options.add_argument("--disable-notifications")

    # Reduce mensajes de que el navegador está siendo controlado.
    options.add_experimental_option(
        "excludeSwitches",
        ["enable-automation"]
    )

    options.add_experimental_option(
        "useAutomationExtension",
        False
    )

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver
#funcion que me permite leer mi archivo csv
# necesito pasarle la ruta a mi archivo
def load_user_csv(path):
    #necesito una lista por que el parametrize recibe una lista de tuplas
    #declaro una variable con una lista vacia
    users = []
    #me manda un tipo de dato y yo necesito otro
    #por eso uso 
    with open(path) as file:   
    #este abre y cierra el archivo que le pase
    # y lo guardo en file
    #tengo que cambiar el formato para poder incrustarlo en users
    #para ello declaro una variable e importo una libreria...csv lo hago arriba
        reader = csv.DictReader(file)
        #esto me devuelve un dict de user and pass, todos los datos dentro de mi archivo
        #para ello necesito un for para recorrer todo el dict
        #{
         #   "username":"",
          #  "password":""
       # }
        for row in reader:
            #para inyectar datos en una lista uso la palabra append
            users.append((row["username"],row["password"]))
            # por ultimo necesito devolver los users
    return users


def load_user_json( path):
    users = []

    with open(path) as file:
        data = json.load(file)

        for user in data:
            users.append((user["username"],user["password"]))
    return users