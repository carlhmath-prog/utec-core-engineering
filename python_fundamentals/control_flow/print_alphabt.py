#!/usr/bin/env python3
output = ""
for i in range(ord('a'), ord('z') + 1):
    char = chr(i)
    if char != 'e' and char != 'q':
        output += char
print(output)
