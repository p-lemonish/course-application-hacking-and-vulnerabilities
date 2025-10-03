import base64 as b
from collections import defaultdict
from typing import Counter
from Cryptodome.Cipher import AES

input = open("8.txt").read()
input_decoded = bytes(b.b64decode(input))
blocks = [input_decoded[i:i+16] for i in range(0, len(input_decoded), 16)]
counts = Counter(blocks)

for block, count in counts.most_common(5):
    print(f"{block.hex()}, count:{count}")
