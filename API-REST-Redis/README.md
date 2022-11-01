# Eercicio API REST usando REDIS

En el desarrollo de este taller, se creó un API REST que usa el motor de REDIS para almacenar la información enviada. Esta se envía a través de un Post que contiene 2 parámetros, el primero es el código del estudiante y el segundo sus datos básicos (nombre, email, carrera, nivel). 

El API se consulta con un GET que reciba como parámetro el código de estudiante y retorna la información asociada al mismo en un JSON.

El despliegue de Redis se realizó a través de un contenedor Docker.

A continuación se muestra la implementación realizada.
