import socket
import _thread

def clientThread(clientSocket):
    while True:
        try:
            msg = clientSocket.recv(2048).decode('ascii')
            if not msg:
                break
            for c in clients:
                if c != clientSocket:
                    c.send(msg.encode('ascii'))
        except:
            clients.remove(clientSocket)
            clientSocket.close()
            break

clients = []
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '127.0.0.1'
port = 8900
serverSocket.bind((host, port))
serverSocket.listen(2)

while True:
    clientSocket, addr = serverSocket.accept()
    clients.append(clientSocket)
    _thread.start_new_thread(clientThread, (clientSocket,))
