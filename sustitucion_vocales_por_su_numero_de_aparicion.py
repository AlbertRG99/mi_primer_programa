"""
Crea un programa que cambie las vocales por su numero de aparición. Por ejemplo: La string “aurora boreal” se convertiría en “12r3r4 b5r67l”
"""

frase_usuario = input("Introduce una frase y cambiaré sus vocales por el numero de aparición: ")
vocales = ["a", "e", "i", "o", "u"]
contador = 0

for letra in frase_usuario:
    if letra in vocales:
        contador += 1
        frase_usuario = frase_usuario.replace(letra, str(contador), 1)

print(frase_usuario)
