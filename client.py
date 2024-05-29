import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'UTF-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Whatever IP address you found from running ifconfig in terminal.
# SERVER = ""
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Officially connecting to the server.
client.connect(ADDR)

def send_msg():
    while True:
        msg = input()
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        if msg == DISCONNECT_MESSAGE:
                break
        
def receive_msg():
        while True:
                msg_length = client.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = client.recv(msg_length).decode(FORMAT)
                    print(msg)

thread_send = threading.Thread(target=send_msg)
thread_receive = threading.Thread(target=receive_msg)
thread_send.start()
thread_receive.start()
