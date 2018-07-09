frase_original = input("Inserte una frase y le daré la vuelta")
frase_reversa = ""
contador = len(frase_original)

while contador >= 0:
    for letra in frase_original:
        contador -= 1
        frase_reversa += frase_original[contador]

print(frase_reversa)