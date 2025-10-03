import base64 as b

input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
input_bytes = bytes.fromhex(input) 
output = b.b64encode(input_bytes)

print(input_bytes)
print(output)
