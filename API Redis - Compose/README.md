# Taller: Api-Rest con Flask y Redis, con Docker compose

En el desarrollo de este taller, se creó un API REST que usa el motor de REDIS para almacenar la información enviada. Esta se envía a través de un Post que contiene 2 parámetros, el primero es el código del estudiante y el segundo sus datos básicos (nombre, email, carrera, nivel). 

Despues de crear la app.py.

## Contenerizar la api en redis con docker compose
Se deben crear un dockerfiles, docker-compose.yaml y un requirements.txt
un Dockerfile para construir la imagen de la aplicación Python Flask. La implementación de un contenedor de Redis para el almacenamiento en caché no requiere un Dockerfile porque usaremos la imagen oficial de Redis Docker de Docker Hub. La imagen oficial también se conoce como imagen base/principal.
También crearemos un archivo `requirements.txt` en la carpeta.

El archivo `docker-compose.yml` que configurará los contenedores de la aplicación como servicios. También agrega todas las configuraciones necesarias para ejecutar 
