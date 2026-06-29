import logging
import os
# Importa el módulo logging para registrar eventos,
# errores y mensajes de ejecución.

# Importa el módulo os para trabajar con carpetas y archivos.

# Crea la carpeta "logs" si no existe.
# exist_ok=True evita que lance una excepción si ya existe.

#logger nos sirve para registrar un historial

#config nos permite crear una carpeta, dando una config basica.

os.makedirs("logs", exist_ok=True) #fileExistsError 
# Configuración principal del sistema de logs.
logging.basicConfig(
    # Archivo donde se guardarán los registros.
    filename="logs/execution.log",
    level=logging.INFO,
    # Formato que tendrá cada línea del log.
    # asctime -> fecha y hora
    # levelname -> nivel del mensaje
    # message -> texto del mensaje
    #funcName-> Función que ejecutó el log
    #filename -> archivo donde ocurrió
    format="%(asctime)s | %(levelname)-8s | %(filename)s | %(funcName)s | %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
    # Fuerza la reconfiguración del logging.
    # Útil cuando ya existía una configuración previa.
    force=True
)
# Obtiene un logger asociado al módulo actual.
# __name__ suele tomar el nombre del archivo Python.
logger = logging.getLogger(__name__)