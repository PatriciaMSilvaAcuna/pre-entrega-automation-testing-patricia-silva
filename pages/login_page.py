from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By


#creo clase de loginpage
class LoginPage:
    #declaro variable para almacenar la url, para luego si tengo que cambiarla lo hago desde aqui.

    URL = "https://www.saucedemo.com/"
    # creo variables para almacenar usuario y contraseña
    # para ello uso el _, variable privada
    # indico con que selector lo ubico 
    # CAPTURA LO ID EN MY PAG WEB
    _USERNAME = (By.ID, "user-name")
    _PASSWORD = (By.ID, "password")
    _LOGIN_BTN = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR,"[data-test='error']")

   
    #declaro constructor
    def __init__(self, driver):
        # Guarda la instancia del navegador.
        self.driver = driver
        
        # Espera explícita para sincronizar las acciones.
        self.wait = WebDriverWait(driver, 10)
    
    #creo metodo que abra el navegador con tal url

    def open(self):
        self.driver.get(self.URL)
    
    #Realizo el login con las credenciales recibidas
    def login(self, username, password):
         
         self.wait.until(
        EC.presence_of_element_located(self._USERNAME)).send_keys(username)

  
        # Espera explícita para asegurar la presencia de los campos
         self.wait.until(
        EC.presence_of_element_located(self._PASSWORD)).send_keys(password)
         self.wait.until(
        EC.presence_of_element_located(self._LOGIN_BTN)).click()
    
    # Devuelve el mensaje mostrado cuando el login es inválido.
    def obtener_error(self):
        return self.wait.until(
        EC.visibility_of_element_located(self._ERROR_MESSAGE)
    ).text