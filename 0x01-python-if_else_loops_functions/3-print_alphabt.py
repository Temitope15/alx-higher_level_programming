#!/usr/bin/python3
for letters in range(97, 123):
    if chr(letters) == 'q' or chr(letters) == 'e':
        continue
    print(chr(letters).format(letters), end='')
