from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """
    Page Object correspondiente al carrito de compras.
    Contiene las acciones y validaciones del carrito.
    """

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    REMOVE = (By.ID, "remove-sauce-labs-backpack")

    def __init__(self, driver):
        # Guarda la instancia del navegador.
        self.driver = driver

        # Espera explícita de hasta 30 segundos.
        self.wait = WebDriverWait(driver, 30)

    def add_product(self):
        """Agrega la mochila al carrito."""
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

    def open_cart(self):
        """Abre el carrito."""
        self.wait.until(
            EC.element_to_be_clickable(self.CART)
        ).click()

    def get_cart_badge(self):
        """Devuelve la cantidad de productos del carrito."""
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text

    def get_product_name(self):
        """Devuelve el nombre del producto agregado."""
        return self.wait.until(
            EC.visibility_of_element_located(self.ITEM_NAME)
        ).text

    def delete_product(self):
        """Elimina el producto del carrito."""
        self.wait.until(
            EC.element_to_be_clickable(self.REMOVE)
        ).click()

    def is_cart_empty(self):
        """Verifica si el carrito quedó vacío."""
        return len(self.driver.find_elements(*self.CART_BADGE)) == 0