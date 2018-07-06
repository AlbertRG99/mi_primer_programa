"""
Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se convertiría en “12r3r4 b5r67l”
"""

frase_usuario = input("Inserta una frase y sustituiré las vocales por su numero de habitación: ")
vocales = ["a", "e", "i", "o", "u"]

while frase_usuario != "FIN":
    contador = 0
    for letra in frase_usuario:
        if letra in vocales:
            frase_usuario = frase_usuario.replace(letra, str(contador + 1))

print(frase_usuario)