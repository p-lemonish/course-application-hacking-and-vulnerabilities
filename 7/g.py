import base64 as b
from Cryptodome.Cipher import AES

input = open("7.txt").read()
input_decoded = bytes(b.b64decode(input))
key = b"YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)
output = cipher.decrypt(input_decoded)

print(str(output))
