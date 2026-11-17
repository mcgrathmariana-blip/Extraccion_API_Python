# Extracción y Almacenamiento Seguro de Datos vía API

## 1. Descripción del proyecto

Este proyecto realiza la extracción de datos desde una API pública utilizando Python. Los datos obtenidos se transforman, se filtran y se almacenan en un archivo JSON estructurado.

El objetivo es demostrar un proceso básico de integración de datos mediante API, incorporando manejo de errores y configuración mediante variables de entorno.

## 2. API utilizada

- **Nombre:** JSONPlaceholder
- **Endpoint:** https://jsonplaceholder.typicode.com/users
- **Método HTTP:** GET
- **Datos obtenidos:** información de usuarios.

## 3. Tecnologías utilizadas

- Python
- Requests
- JSON
- Python-dotenv
- Google Colab

## 4. Estructura del proyecto

- `extract_data.py`: script principal de extracción y transformación.
- `Extraccion_API_Python.ipynb`: notebook con el desarrollo y las pruebas.
- `data_extracted.json`: datos extraídos y transformados.
- `.env.example`: plantilla de configuración de variables de entorno.
- `.gitignore`: exclusión de archivos privados y temporales.
- `requirements.txt`: dependencias necesarias para ejecutar el proyecto.

## 5. Proceso de extracción y transformación

El script realiza las siguientes operaciones:

1. Carga la URL de la API desde una variable de entorno.
2. Realiza una solicitud HTTP GET.
3. Verifica que la respuesta sea exitosa.
4. Obtiene los datos en formato JSON.
5. Filtra y transforma los campos de cada usuario.
6. Guarda los resultados en `data_extracted.json`.

Se conservaron los siguientes campos:

- ID
- Nombre
- Nombre de usuario
- Email
- Ciudad
- Empresa

## 6. Manejo de errores

Se incorporaron controles para gestionar:

- Errores HTTP, como respuestas 404 o 500.
- Tiempo de espera agotado.
- Errores de conexión.
- Problemas durante el procesamiento de los datos.

Se realizaron pruebas con un endpoint inexistente para verificar el manejo de errores HTTP.

## 7. Configuración y seguridad

La URL de la API se configura mediante la variable de entorno `API_URL`.

El archivo `.env` contiene la configuración local y está excluido del repositorio mediante `.gitignore`.

Para comenzar, se debe crear un archivo `.env` a partir de `.env.example` y configurar la variable `API_URL`.

No se deben publicar archivos `.env` ni credenciales privadas.

## 8. Instalación y ejecución

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Crear un archivo `.env` a partir de `.env.example` y configurar:

```env
API_URL=https://jsonplaceholder.typicode.com/users
```

Ejecutar el script:

```bash
python extract_data.py
```

El resultado se almacena en el archivo data_extracted.json en la raíz del proyecto.

## 9. Resultado

La ejecución de la extracción obtuvo correctamente 10 registros de usuarios, que fueron transformados y almacenados en formato JSON.

## 10. Autoría

Proyecto académico desarrollado como práctica de extracción, transformación y almacenamiento de datos mediante API.
