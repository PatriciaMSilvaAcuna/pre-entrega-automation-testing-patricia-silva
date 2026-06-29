# 🚀 Proyecto Final QA Automation

Framework de automatización de pruebas desarrollado en **Python**, utilizando **Pytest**, **Selenium WebDriver** y **Requests**, aplicando el patrón de diseño **Page Object Model (POM)**.

El proyecto automatiza pruebas funcionales de **UI** sobre **SauceDemo** y pruebas de **API REST** sobre **Reqres**, incluyendo reportes HTML, logging, parametrización de datos y capturas de pantalla automáticas en caso de error.

---

# 📌 Tecnologías utilizadas

* Python 3.x
* Selenium WebDriver
* Pytest
* Pytest-Check
* Requests
* Faker
* WebDriver Manager
* Pytest HTML Report

---

# 📂 Estructura del proyecto

```text
Pre_entrega_QA/
│
├── api/
│   └── api_client.py
│
├── data/
│   ├── users.csv
│   └── users.json
│    └── invalid_users.json

│
├── logs/
│   └── execution.log
│
├── pages/
│   ├── login_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   └── report.html
│
├── screenshots/
│
├── tests/
│   ├── test_all.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login_negative.py
│
├── utils/
│   ├── helpers.py
│   └── logger.py
│
├── conftest.py
├── pytest.ini
└── README.md
```

---

# 🧪 Casos de prueba implementados

## UI - SauceDemo

✔ Login válido

✔ Login inválido

✔ Agregar producto al carrito

✔ Eliminar producto del carrito

✔ Checkout completo

---

## API - Reqres

✔ Obtener usuarios

✔ Crear usuario

✔ Login exitoso

---

# 📁 Datos de prueba

Los datos se encuentran externalizados en archivos:

* JSON
* CSV

Utilizando `pytest.mark.parametrize()` para ejecutar los mismos casos de prueba con distintos datos.

---

# 🏗 Patrón de diseño

Se implementó **Page Object Model (POM)** para separar:

* Localizadores
* Acciones sobre la página
* Casos de prueba

Esta arquitectura facilita el mantenimiento y la reutilización del código.

---

# 📋 Reportes

El proyecto genera automáticamente un reporte HTML mediante **pytest-html**.

Ubicación:

```text
reports/report.html
```

---

# 📸 Capturas de pantalla

Cuando una prueba falla, se almacena automáticamente una captura en:

```text
screenshots/
```

El nombre del archivo incluye el nombre del test y la fecha de ejecución.

---

# 📝 Logging

Se registra la ejecución de los tests mediante el módulo **logging**, incluyendo:

* Inicio del test
* Acciones realizadas
* Datos generados con Faker
* Resultado final

Los logs se almacenan en:

```text
logs/execution.log
```

---

# ▶ Cómo instalar

Crear un entorno virtual:

```bash
python -m venv venv
```

Activarlo:

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# ▶ Ejecutar todas las pruebas

```bash
pytest
```

---

# ▶ Ejecutar únicamente pruebas API

```bash
pytest tests/test_all.py -v
```

---

# ▶ Ejecutar únicamente pruebas UI

Checkout

```bash
pytest tests/test_checkout.py -v
```

Carrito

```bash
pytest tests/test_cart.py -v
```

Login negativo

```bash
pytest tests/test_login_negative.py -v
```

---

# ▶ Generar reporte HTML

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# 💡 Mejoras futuras

* Integración continua con GitHub Actions.
* Ejecución en Docker.
* Reportes Allure.
* Ejecución Cross Browser (Chrome, Edge y Firefox).
* Ejecución paralela con pytest-xdist.

---

# 👩‍💻 Autor

**Patricia Silva**

Proyecto desarrollado como trabajo final de Automatización QA utilizando Selenium, Pytest y Requests.
