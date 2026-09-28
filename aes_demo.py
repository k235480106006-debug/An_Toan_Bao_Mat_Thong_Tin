from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Khởi tạo khóa và IV (16 bytes = 128-bit)
key = b'1234567890123456'
iv = b'1234567890123456'
plaintext = b"Hello TNUT - An Toan Bao Mat Thong Tin"

# Quy trình mã hóa AES (chế độ CBC)
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
print("Dữ liệu sau mã hóa (Hex):", ciphertext.hex())

# Quy trình giải mã AES
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Dữ liệu sau giải mã:", decrypted.decode('utf-8'))