import base64 as b

input = "1c0111001f010100061a024b53535009181c"
input_bytes = bytes.fromhex(input) 
xor_key = "686974207468652062756c6c277320657965"
xor_key_bytes = bytes.fromhex(xor_key)

print(xor_key_bytes)
print(input_bytes)
output = ""
for i in range(len(xor_key_bytes)):
    a = xor_key_bytes[i]
    b = input_bytes[i]
    print(f'{a}^{b} = {a^b}')
    output += chr(a ^ b)

print(output)
