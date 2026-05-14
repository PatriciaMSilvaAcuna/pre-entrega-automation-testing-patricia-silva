from utils.helpers import login


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#funcion que testea el login
def test_login( driver ):
    login(driver, "standard_user", "secret_sauce")
   # valida redirección al inventario
    
    # valida acceso exitoso al inventario
    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text
    # valida título de inventario   
    assert title == "Products"

def test_catalog_products( driver):
    login(driver, "standard_user", "secret_sauce")

    title = driver.find_element(By.CLASS_NAME, "title").text
    assert title == "Products"
    # obtiene listado de productos visibles
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test = 'inventory-item']")
    
    # valida existencia de productos en catálogo
    assert len(productos) > 0 

    nombre = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert nombre == "Sauce Labs Backpack"
    
    precio = productos[0].find_element(By.CSS_SELECTOR, "[data-test='inventory-item-price']"
    ).text
    
    
    print(f"Precio: {precio}")
    # valida elementos principales de interfaz

    #Presencia de filtro
    filter_product = driver.find_element(By.CLASS_NAME, "product_sort_container") 
    assert filter_product.is_displayed()
    #Presencia del menú
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu.is_displayed()

def test_add_to_cart(driver):
    login(driver, "standard_user", "secret_sauce")
    # obtiene nombre del producto seleccionado
    name_product = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    
    # espera explícita hasta que el botón sea clickeable
    
    wait = WebDriverWait(driver,10)
    # espera botón Add to cart clickeable
   
    btn_add = wait.until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add to cart')]"))
    )
    
     # agrega producto al carrito
    btn_add.click()
    

    #valida el contador del carrito

    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    # navega al carrito de compras

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    
    #valida producto del carrito
    
    product_cart = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert product_cart == name_product
