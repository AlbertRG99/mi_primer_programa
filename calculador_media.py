"""
Crea un programa que calcule la media de los elementos de la lista de números (media = suma de todos los numeros / numero de numeros )
"""
numeros_media= [11, 21, 3, 42, 3, 2]

cuantos_numeros=len(numeros_media)

todos_numeros=0

for e in numeros_media:

    todos_numeros+=e

resultado = todos_numeros / cuantos_numeros

print("La media de {} es {}".format(numeros_media,resultado))