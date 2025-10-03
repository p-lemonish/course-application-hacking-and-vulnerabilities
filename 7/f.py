import base64 as b
from collections import defaultdict

input_file = open("6.txt").read()
input_decode = b.b64decode(input_file)

def hamming_distance(byte_str1, byte_str2):
    distance = 0
    for i in range(len(byte_str1)): # oletus: str1 ja str2 samanpituiset
        xor_res = byte_str1[i] ^ byte_str2[i]
        bits = xor_res.bit_count()
        distance += bits
    return distance

key_dist = {}
for keysize in range(2, 41):
    str1 = input_decode[0:keysize]
    str2 = input_decode[keysize:2*keysize]
    str3 = input_decode[2*keysize:3*keysize]
    str4 = input_decode[3*keysize:4*keysize]
    distances = [
        hamming_distance(str1, str2),
        hamming_distance(str1, str3),
        hamming_distance(str1, str4),
        hamming_distance(str2, str3),
        hamming_distance(str2, str4),
        hamming_distance(str3, str4),
    ]
    dist_avg = sum(distances) / len(distances)
    normalized = dist_avg/keysize
    key_dist[keysize] = normalized
    #print(f"keysize: {keysize}, normalized: {dist_avg/keysize}")

print("Best keysize performers:")
best_five = sorted(key_dist, key=key_dist.get)[:5]
print(best_five)

def chunk_blocks(cipher, keysize):
    return [cipher[i:i+keysize] for i in range(0, len(cipher), keysize)]

# ymmärtämisen helpottamiseksi, tehdään yksi keysize kerrallaan
best = best_five[0]
blocks = chunk_blocks(input_decode, best)

def transpose_blocks(blocks, ks):
    cols = [[] for _ in range(ks)]
    for block in blocks:
        for i in range(ks):
            if i < len(block):
                cols[i].append(block[i])
    return cols

transposed_blocks = transpose_blocks(blocks, best)
#print(f"{blocks}\n{transposed_blocks}")

# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
# lisätty pikkukirjaimet myös suoraan
letterFrequency = {'E' : 12.0, 'T' : 9.10, 'A' : 8.12, 'O' : 7.68,
'I' : 7.31, 'N' : 6.95, 'S' : 6.28, 'R' : 6.02, 'H' : 5.92, 'D' : 4.32,
'L' : 3.98, 'U' : 2.88, 'C' : 2.71, 'M' : 2.61, 'F' : 2.30, 'Y' : 2.11,
'W' : 2.09, 'G' : 2.03, 'P' : 1.82, 'B' : 1.49, 'V' : 1.11, 'K' : 0.69,
'X' : 0.17, 'Q' : 0.11, 'J' : 0.10, 'Z' : 0.07, 'e' : 12.0, 't' : 9.10,
'a' : 8.12, 'o' : 7.68, 'i' : 7.31, 'n' : 6.95, 's' : 6.28, 'r' : 6.02,
'h' : 5.92, 'd' : 4.32, 'l' : 3.98, 'u' : 2.88, 'c' : 2.71, 'm' : 2.61,
'f' : 2.30, 'y' : 2.11, 'w' : 2.09, 'g' : 2.03, 'p' : 1.82, 'b' : 1.49,
'v' : 1.11, 'k' : 0.69, 'x' : 0.17, 'q' : 0.11, 'j' : 0.10, 'z' : 0.07 }
letterFrequency[' '] = 15.0
letterFrequency['.'] = 0.5
letterFrequency[','] = 0.5
letterFrequency['!'] = 0.5
letterFrequency['?'] = 0.5
letterFrequency["'"] = 0.5
letterFrequency["-"] = 0.5
xor_key = ""

for t_block in transposed_blocks:
    outputs = defaultdict(list)
    for i in range(255): 
        output = ""
        points = 0
        for b in t_block:
            char_out = b ^ i
            if chr(char_out) in letterFrequency.keys():
                points += letterFrequency[chr(char_out)]
            output += chr(char_out)
        outputs[points].append(i)
    highest_points = max(outputs)
    xor_key += chr(outputs[highest_points][0])
        
print(xor_key)
