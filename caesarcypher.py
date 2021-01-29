#!/usr/bin/env python3.8
target = input("Ingrese el texto que desea cifrar: ").split()
cypher = []
n = 0

for word in target:
    cypher.append([])
    for letter in word:
        ucode = ord(letter)
        if ucode >= 65 and ucode <= 90:
            cypher[n].append(chr(ucode - 13)) if ucode > 77 else cypher[n].append(chr(ucode + 13))
        elif ucode >= 97 and ucode <= 122:
            cypher[n].append(chr(ucode - 13)) if ucode > 109 else cypher[n].append(chr(ucode + 13))
        else: 
            print('Este script solo soporta los rangos [a-z][A-Z]. No numeros ni caracteres especiales.')
            exit(1)
    cypher[n] = ''.join(cypher[n])
    n += 1

cypher = " ".join(cypher)

print(cypher)