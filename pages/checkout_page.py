from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from faker import Faker


#herramienta para config los datos
fake = Faker("es_AR")



class CheckoutPage:
    #declaro variable para ubicar el elemento
    # variable privada
    ADD_TO_CART = (By.ID,"add-to-cart-sauce-labs-backpack")
    GO_TO_CART = (By.CLASS_NAME,"shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID,"checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID,"last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID,"continue")
    FINISH = (By.ID,"finish")
    COMPLETE_SUCCESS = (By.CLASS_NAME, "complete-header")

    # defino el contructor que almacena la variable del driver 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,30)


    def add_product(self):
        self.driver.find_element(*self.ADD_TO_CART).click()

    def go_cart(self):
        self.driver.find_element(*self.GO_TO_CART).click()
    
    def init_cart(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def complete_form(self):
        #llamamos a los metodos que necesitamos

        first_name = fake.first_name()
        last_name = fake.last_name()
        postal_code = fake.postal_code()

        print(first_name,last_name,postal_code)

     #   self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
      #  self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
       # self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.wait.until(
          EC.presence_of_element_located(self.FIRST_NAME)

        ).send_keys(first_name)
        self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME)

        ).send_keys(last_name)
        self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE)
        ).send_keys(postal_code)


    def continuar(self):
        self.driver.find_element(*self.CONTINUE).click()
    def finish(self):
        self.driver.find_element(*self.FINISH).click()
    def mensaje_exito(self):
        self.driver.find_element(*self.COMPLETE_SUCCESS).click()