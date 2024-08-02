import socket  # socket: Librería para manejar conexiones de red.
import threading  # threading: Se usa para manejar múltiples hilos de ejecución.

username = input("Ingresa tu username: ")  # Solicita al usuario que ingrese su nombre de usuario.

host = '127.0.0.1'  # Dirección IP del servidor al que se conecta.
port = 12345  # Puerto del servidor al que se conecta.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket para el cliente.
client.connect((host, port))  # Conecta el socket del cliente al servidor.

def receive_message():  # Función para recibir mensajes del servidor.
    while True:
        try:
            message = client.recv(1024).decode('utf-8')  # Recibe un mensaje del servidor.

            if message == "@username":  # Si el mensaje es "@username", el servidor solicita el nombre de usuario.
                client.send(username.encode("utf-8"))  # Envía el nombre de usuario al servidor.
            else:
                print(message)  # Imprime el mensaje recibido.
        except:
            print("Ocurrió un error")  # Imprime un mensaje de error si ocurre una excepción.
            client.close()  # Cierra la conexión del cliente.
            break  # Sale del bucle.

def write_message():  # Función para enviar mensajes al servidor.
    while True:
        message = f"{username}: {input('')}"  # Toma el mensaje del usuario.
        client.send(message.encode('utf-8'))  # Envía el mensaje al servidor.

# CREA UN HILO PARA RECIBIR MENSAJES
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()  # Inicia el hilo para recibir mensajes.

# CREA UN HILO PARA ENVIAR MENSAJES
write_thread = threading.Thread(target=write_message)
write_thread.start()  # Inicia el hilo para enviar mensajes.
