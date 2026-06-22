# Importa la librería requests, que permite realizar solicitudes HTTP
# (GET, POST, PUT, DELETE, etc.) desde Python.
import requests
# URL del endpoint al que vamos a enviar la solicitud.
# En este caso es el endpoint de login de Reqres.
URL_BASE = "https://reqres.in/api/login"

# Headers de la solicitud.
# Los headers contienen información adicional que la API necesita.
# En este caso enviamos la API Key para autenticarnos.

HEADER ={
    "x-api-key": "free_user_3EYBQ5bAIz7xQInpk603z2kzmDR",



}
# Datos que se enviarán en el Body de la petición.
# Simulan las credenciales de un usuario que quiere iniciar sesión.
creds = {
     'email': 'eve.holt@reqres.in',
     'password': 'cityslicka'


}

#def get_users():
 #   response = requests.get(URL_BASE,headers=HEADER)
#    #puedo hacer validaciones
#
#    if response.status_code == 200:
#       print(response.json())
#    else:
#        print("error")

#    print(response.status_code)


#get_users()
# Función que realiza un login mediante una petición POST.
def login_post():
    # Envía una solicitud POST al endpoint de login.
    #
    # URL_BASE  -> endpoint al que se envía la petición
    # headers   -> información adicional (API Key)
    # json      -> datos enviados en el Body
    result = requests.post(URL_BASE, headers=HEADER,json=creds)

    # Muestra el código de estado HTTP devuelto por la API.
    #
    # Ejemplos:
    # 200 = OK
    # 400 = Bad Request
    # 401 = Unauthorized
    # 404 = Not Found
    # 500 = Internal Server Error
    print("Status Code:", result.status_code)

    # Convierte la respuesta JSON en un diccionario de Python.
    response_body = result.json()

    # Muestra el contenido completo de la respuesta.
    print("Response:", result.json())


    # Validación básica:
    # Si el código de respuesta es 200,
    # consideramos que el login fue exitoso.
    if result.status_code == 200:
        print("Login exitoso")

        # Obtiene el token devuelto por la API.
        # El token suele utilizarse para acceder
        # a otros endpoints protegidos.
        print("Token:", result.json()["token"])
    else:
         # Si la respuesta no es 200,
        # informamos que ocurrió un error.
        print("Error en el login")


# Ejecuta la función para probar el login.
login_post()