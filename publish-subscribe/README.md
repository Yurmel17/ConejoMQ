# Publish/Subscribe

Creación de un broker de mensajería usando RabbitMQ. 

En el proceso, se crearon dos productores (P1 y P2), en python y node respectivamente. P1 envía mensajes a los canales A y B, mientras que P2 envía únicamente al canal B.

Por el lado de los consumidores, tenemos dos en python (C2 y C3) y uno en node (C1). C1 y C2 reciben mensajes de los canales A y B respectivamente, y C3 recibe de ambos canales.

A continuación se deja la implementación y un pdf con las pruebas realizadas
