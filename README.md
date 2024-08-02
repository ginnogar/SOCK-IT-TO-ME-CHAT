El código implementa un servidor y un cliente de chat en Python utilizando sockets y multihilos. El servidor escucha conexiones entrantes en 127.0.0.1 y el puerto 12345, gestionando 
múltiples clientes a la vez. Cada cliente que se conecta envía su nombre de usuario y puede enviar mensajes que se retransmiten a todos los demás clientes conectados. El servidor maneja 
desconexiones inesperadas eliminando al cliente de las listas de clientes y nombres de usuario y notificando a los demás usuarios. El cliente se conecta al servidor, envía su nombre 
de usuario y me permite enviar y recibir mensajes en tiempo real a través de hilos separados para la recepción y el envío de mensajes.
