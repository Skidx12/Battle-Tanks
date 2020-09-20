from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b'mypasswordsecret'
cipher = AES.new(key,AES.MODE_CBC)

plaintxt =b'this is my secret message'

ciphertext = cipher.encrypt(pad(plaintxt,AES.block_size))

#print(ciphertext)

with open('cipher_file', 'w') as c_file:
    c_file.write(cipher.iv)
    c_file.write(ciphertext)