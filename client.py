import socket
import threading

name = input("Enter your name >> ")
HOST = '192.168.29.249'
PORT = 57889

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def recvi():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'id':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('error occurred')
            client.close()
            break

def write():
    while True:
        message = f'{name}:{input(" ")}'
        client.send(message.encode('utf-8'))

re = threading.Thread(target=recvi)
wr = threading.Thread(target=write)
re.start()
wr.start()
