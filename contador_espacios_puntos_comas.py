"""
Crea un programa capaz de contar espacios, puntos y comas en una string introducida por el usuario.
"""

frase_del_usuario = input("Introduce una frase: ")

espacios = " "
puntos = "."
comas = ","

numero_espacios = 0
numero_puntos = 0
numero_comas = 0

for letra in frase_del_usuario:
    if letra in espacios:
        numero_espacios += 1
    if letra in puntos:
        numero_puntos += 1
    if letra in comas:
        numero_comas += 1

print("Espacios: {}".format(numero_espacios))
print("Puntos: {}".format(numero_puntos))
print("Comas: {}".format(numero_comas))