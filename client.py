import socket

HEADER = 1024
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.8" #address of server host
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET for ipv4 connection and SockStraem for streaming messages continuously
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) #when the message is shorter than the defined size(bytes), we need padding. here, padding with blank spaces.
    client.send(send_length)
    client.send(message)
    print("RECV: ",client.recv(2048).decode(FORMAT))

while True:
    print(">>> ")
    send(input())
    print("\n")

send(DISCONNECT_MESSAGE)


