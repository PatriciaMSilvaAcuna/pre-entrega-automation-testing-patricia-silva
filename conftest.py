import pytest
from utils.helpers import get_driver
#creo fixture que me permita crear el driver 
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    #cierro sesion 
    driver.quit()