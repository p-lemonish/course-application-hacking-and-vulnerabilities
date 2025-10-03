import base64 as b
from collections import defaultdict

input_list = open("4.txt").readlines()
input_list_bytes = [bytes.fromhex(line) for line in input_list]
top_outputs = {}
line = 0

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

for input_bytes in input_list_bytes:
    outputs = defaultdict(list)
    for i in range(255): 
        output = ""
        points = 0
        for b in input_bytes:
            char_out = b ^ i
            if chr(char_out) in letterFrequency.keys():
                points += letterFrequency[chr(char_out)]
            output += chr(char_out)
        outputs[points].append(f"XOR with {i}: {output}")
    highest_points = max(outputs.keys())
    top_outputs[line] = (highest_points, outputs[highest_points])
    line += 1
        
global_max = max(points for points, _ in top_outputs.values())
best_lines = [
    (line, outputs) for (line, (points, outputs)) in top_outputs.items()
    if points == global_max
]
print(f"best guess: {best_lines}")
