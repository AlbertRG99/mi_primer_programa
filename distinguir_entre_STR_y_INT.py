"""
Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.
"""

lista_mixta = [1, "hola", 23, 567, "adios", 4, "veinticinco"]
lista_enteros = []
lista_strings = []

for elemento in lista_mixta:
    if isinstance(elemento, str) is True:
        lista_strings.append(elemento)
    else:
        lista_enteros.append(elemento)

print(lista_enteros)
print(lista_strings)
#"isinstance(elemento, str)" y presiona "Enter". Esta línea pregunta si "elemento" es un carácter.
# Python responde "Verdadero/Falso". También existe "isinstance(elemento, int)" #