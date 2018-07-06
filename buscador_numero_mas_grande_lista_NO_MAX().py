lista = [1, 2, 5, 6, 9, 45, 67, 2, 565, 8686, 19]
alto = lista[0]

for numero in lista:
    if numero > alto:
        alto = numero

print("El número más grande de la lista es: {}".format(alto))