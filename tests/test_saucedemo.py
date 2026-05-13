from utils.helpers import login
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login( driver ):
    login(driver, "standard_user", "secret_sauce")
    #validamos que x está en la url
    time.sleep(5)
    assert"inventory.html" in driver.current_url
    

 