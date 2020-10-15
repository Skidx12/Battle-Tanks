import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad



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

while True:
    print(">>> ")
    send(input("Send :",))
    print("\n")

send(DISCONNECT_MESSAGE)


