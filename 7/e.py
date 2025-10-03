import base64 as b
from collections import defaultdict

input = "Burning 'em, if you ain't quick and nimble \
        I go crazy when I hear a cymbal"
xor_key = "ICE"
output = ""
i = 0

for byte in input:
    #print(f"XOR {byte} ^ {xor_key[i%len(xor_key)]} : {chr(ord(byte) ^ ord(xor_key[i % len(xor_key)]))} : {ord(byte) ^ ord(xor_key[i % len(xor_key)])}")
    output += f"{ord(byte) ^ ord(xor_key[i % len(xor_key)]):02x}"
    i += 1

print(output)
