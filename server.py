import socket

import threading

HOST = '192.168.29.249'
PORT = 57889
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print('SERVER RUNNING.....')

clients = []
names = []


def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))


def task(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            namee = names[index]
            broadcast(f"{namee} left the chat")
            names.remove(namee)
            break


def Server():
    while True:
        client, address = server.accept()
        print(f'{str(address)} is connected')
        client.send('id'.encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        client.send("Connected to the server".encode('utf-8'))
        broadcast(f'{name} joined the chat')
        clients.append(client)
        names.append(name)

        t = threading.Thread(target=task, args=(client,))
        t.start()


Server()
