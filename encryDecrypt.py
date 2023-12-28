from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def encrypt_des(key, plaintext):
    key = key.ljust(8, ' ')  # Ensure the key is 8 bytes long
    key = key.encode('utf-8')
    plaintext = plaintext.encode('utf-8')

    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    return b64encode(ciphertext).decode('utf-8')

def decrypt_des(key, ciphertext):
    key = key.ljust(8, ' ')  # Ensure the key is 8 bytes long
    key = key.encode('utf-8')
    ciphertext = b64decode(ciphertext)

    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)

    return decrypted_data.decode('utf-8')
