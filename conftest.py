import pytest
import os

from utils.helpers import get_driver
from utils.logger import logger
from datetime import datetime

#creo fixture que me permita crear el driver

# ==========================
# FIXTURE DRIVER (UI)
# ========================== 
@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    #cierro sesion 
    driver.quit()


# ==========================
# FIXTURES API
# ==========================


@pytest.fixture
def posts_data():
    return {
        "title": "Mi Pimer Posteo",
        "body": "Contindo de mi primer post",
        "userId": 1
    }


@pytest.fixture
def users_data():
    return {
        "name": "Patito",
        "job": "Analista & QA"
    }
# ==========================
# TÍTULO DEL REPORTE HTML
# ==========================
def pytest_html_report_title(report):
    report.title = "Proyecto Final QA Automation | UI + API Testing | Reqres"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            fecha = datetime.now().strftime("%Y%m%d_%H%M%S")

            nombre = f"{item.name}_{fecha}.png"

            ruta = os.path.join("screenshots", nombre)

            driver.save_screenshot(ruta)

            logger.error(
            f"Screenshot guardado: {ruta}"
) 