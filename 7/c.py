import base64 as b
from collections import defaultdict

input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
input_bytes = bytes.fromhex(input) 
outputs = defaultdict(list)

for i in range(200): # arvataan, että varmaan jokin ekasta 200:sta merkistä on ollut avaimena
    output = ""
    points = 0
    for b in input_bytes:
        char_out = b ^ i
        if (char_out >= 0x41 and char_out <= 0x5a) or (char_out >= 0x61 and char_out <= 0x7a):
            points += 1
        output += chr(char_out)
    outputs[points].append(f"XOR with {i}: {output}")
        
highest_points = max(outputs.keys())
print(f"best output(s): {outputs[highest_points]}")
