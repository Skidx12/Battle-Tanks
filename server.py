import socket 
import threading

HEADER = 1024
PORT = 5050
SOCKET_NAME = socket.gethostname()
SERVER = socket.gethostbyname(SOCKET_NAME)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET for ipv4 connection and SockStraem for streaming messages continuously
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print("RECV : ")
            print(f"[{addr}] {msg}")
            conn.send(input().encode(FORMAT))

    conn.close()

def encr():
    key = b'mypasswordsecret'
    cipher = AES.new(key,AES.MODE_CBC)

    plaintxt =b'this is my secret message'

    ciphertext = cipher.encrypt(pad(plaintxt,AES.block_size))

    #print(ciphertext)

    with open('cipher_file', 'w') as c_file:
        c_file.write(cipher.iv)
        c_file.write(ciphertext)

def decr():
    
    key = b'mypassword'
    with open('cipher_file', 'rb') as c_file:
        iv = c_file.read(16)
        ciphertext = c_file.read()

    cipher = AES.new(key,AES.MODE_CBC, iv)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print(plaintext.decode())
    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()

