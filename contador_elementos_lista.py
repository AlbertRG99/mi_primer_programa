"""
Crea un programa que cuente los elementos de la lista de números introducida por el usuario. Está prohibido utilizar la función len() para resolver el problema.
"""

lista_usuario = []
contador_elementos = 0

while lista_usuario != "FIN":
    lista_usuario = input("Añade un elemento a la lista: ")
    print("Número añadido con éxito!")
    contador_elementos += 1

contador_elementos -=1
print("Esta lista contiene {} elementos".format(contador_elementos))

