
import requests
import json
import os
from dotenv import load_dotenv

# 1. Cargar variables de entorno
load_dotenv()

API_URL = os.getenv("API_URL")

# 2. Verificar configuración
if not API_URL:
    raise ValueError("No se encontro API_URL en el archivo .env")

# 3. Extraccion de datos
try:
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    usuarios = response.json()

    if not isinstance(usuarios, list):
        raise ValueError("Formato de respuesta inesperado")

    # 4. Transformacion de datos
    usuarios_limpios = []

    for usuario in usuarios:
        usuario_filtrado = {
            "id": usuario["id"],
            "nombre": usuario["name"],
            "usuario": usuario["username"],
            "email": usuario["email"],
            "ciudad": usuario["address"]["city"],
            "empresa": usuario["company"]["name"]
        }

        usuarios_limpios.append(usuario_filtrado)

    # 5. Almacenamiento
    os.makedirs("data", exist_ok=True)

    with open("data/data_extracted.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios_limpios, archivo, indent=4, ensure_ascii=False)

    print("Extraccion realizada correctamente")
    print(f"Usuarios obtenidos: {len(usuarios_limpios)}")
    print("Archivo generado: data/data_extracted.json")

except requests.exceptions.HTTPError as e:
    print(f"Error HTTP: {e}")

except requests.exceptions.Timeout:
    print("Error: tiempo de espera agotado")

except requests.exceptions.ConnectionError:
    print("Error de conexion con la API")

except requests.exceptions.RequestException as e:
    print(f"Error en la peticion: {e}")

except (ValueError, KeyError) as e:
    print(f"Error al procesar los datos: {e}")
