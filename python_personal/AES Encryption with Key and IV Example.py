from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def encrypt_aes(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = plaintext + (AES.block_size - len(plaintext) % AES.block_size) * chr(AES.block_size - len(plaintext) % AES.block_size)
    ciphertext = cipher.encrypt(padded.encode())
    return base64.b64encode(ciphertext).decode('utf-8')

def decrypt_aes(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(base64.b64decode(ciphertext))
    return plaintext[:-plaintext[-1]].decode('utf-8')

# 生成一个16字节（128位）的随机密钥和IV
key = get_random_bytes(16)
iv = get_random_bytes(16)

message = "Hello, AES encryption!"
encrypted = encrypt_aes(message, key, iv)
decrypted = decrypt_aes(encrypted, key, iv)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# 使用相同的密钥，但不同的IV加密相同的消息
iv2 = get_random_bytes(16)
encrypted2 = encrypt_aes(message, key, iv2)

print(f"\nEncrypted with different IV: {encrypted2}")
print(f"Same as first encryption: {encrypted == encrypted2}")