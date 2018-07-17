import os

def pares(list):
    pares = []
    for i in list:
        resto = int(i) % 2
        if resto == 0:
            pares.append(i)
    os.system("cls")
    print("Lista de números pares: ", pares)

def añadirLista():
    enter = True
    lista = []
    while enter == True:
        os.system("cls")
        if len(lista) > 0:
            print("Lista actual: ", lista)
        n = input("Introduzca un número o escriba SALIR para terminar: ")
        if n == "SALIR":
            enter = False
            pares(lista)
        lista.append(n)
añadirLista()
