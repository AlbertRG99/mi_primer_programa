"""
Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario.
"""

frase_del_usuario = input("Escribe una frase para todas sus vocales: ")

vocales = ["a", "e", "i", "o", "u"]

for letra in frase_del_usuario:
    if letra in vocales:
        print(letra)