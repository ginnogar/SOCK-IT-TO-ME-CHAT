import socket  # Socket: Es un punto final para enviar y recibir datos a través de una red.
import threading  # threading: Se usa para manejar múltiples hilos de ejecución.

# Connection Data
host = '127.0.0.1'  # La dirección IP del host donde se ejecuta el servidor. 
port = 12345  # El puerto en el que el servidor escuchará las conexiones entrantes.

# Crear el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: Esto especifica que usaremos direcciones IPv4. Las direcciones IPv4 son un tipo de dirección IP utilizada para identificar dispositivos en una red
# socket.SOCK_STREAM: Esto especifica que usaremos el protocolo TCP. TCP es un protocolo de comunicación que permite la transmisión de datos entre dispositivos

# Enlazar el socket a una dirección IP y un puerto
server_socket.bind((host, port))  # Enlaza el socket a la dirección IP y puerto especificados.

# Escuchar conexiones
server_socket.listen()  # Pone el servidor en modo escucha para nuevas conexiones.

print("Servidor de chat iniciado en el puerto 12345. Esperando conexiones...")

clients = []  # Lista para almacenar los sockets de los clientes conectados.
usernames = []  # Lista para almacenar los nombres de usuario de los clientes conectados.

def broadcast(message, _client):  # Enviar un mensaje a todos los clientes excepto al que lo envió.
    for client in clients:  # Itera sobre la lista de clientes.
        if client != _client:  # Si el cliente no es el que envió el mensaje.
            client.send(message)  # Envía el mensaje.

def handle_message(client):  # Manejar los mensajes de cada cliente.
    while True:
        try:
            message = client.recv(1024)  # Recibe un mensaje del cliente.
            broadcast(message, client)  # Difunde el mensaje a todos los demás clientes.
        except:
            index = clients.index(client)  # Obtiene el índice del cliente en la lista.
            username = usernames[index]  # Obtiene el nombre de usuario correspondiente.
            broadcast(f'ChatBot: {username} desconectado'.encode('utf-8'))  # Informa a los demás clientes.
            clients.remove(client)  # Elimina el cliente de la lista de clientes.
            usernames.remove(username)  # Elimina el nombre de usuario de la lista.
            client.close()  # Cierra la conexión del cliente.
            break  # Sale del bucle.

def receive_connections():  # Acepta nuevas conexiones de clientes.
    while True:
        client, address = server_socket.accept()  # Acepta una nueva conexión.
        client.send("@username".encode("utf-8"))  # Solicita el nombre de usuario al nuevo cliente.
        username = client.recv(1024).decode('utf-8')  # Recibe el nombre de usuario del cliente.

        clients.append(client)  # Añade el nuevo cliente a la lista de clientes.
        usernames.append(username)  # Añade el nombre de usuario a la lista de nombres.

        print(f'{username} se conecto con {str(address)}')  # Imprime un mensaje en el servidor.

        message = f"ChatBot: {username} entro al chat!".encode("utf-8")  # Crea un mensaje de bienvenida.
        broadcast(message, client)  # Difunde el mensaje de bienvenida a todos los clientes.
        client.send("Conectado al servidor".encode("utf-8"))  # Envía un mensaje de confirmación al nuevo cliente.

        # CREA UN HILO PARA MANEJAR LOS MENSAJES DE ESTE CLIENTE
        thread = threading.Thread(target=handle_message, args=(client,))
        thread.start()  # Inicia el hilo.

receive_connections()  # Llama a la función para recibir conexiones.
