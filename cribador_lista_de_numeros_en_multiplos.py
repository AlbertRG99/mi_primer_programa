"""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:

input = [1, 10, 70, 30, 50, 55]

multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 60, 55]
multiplos_siete = [70]
"""

lista = []
lista_usuario = []
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

while lista_usuario != "FIN":
    lista_usuario = input("Escribe los numeros que quieres cribar y pulsa 'FIN' para continuar: ")
    lista.append(lista_usuario)

lista.remove("FIN")

for numero in lista:
    if int(numero) % 2 == 0:
        multiplos_dos.append(int(numero))
    if int(numero) % 3 == 0:
        multiplos_tres.append(int(numero))
    if int(numero) % 5 == 0:
        multiplos_cinco.append(int(numero))
    if int(numero) % 7 == 0:
        multiplos_siete.append(int(numero))

print("MÚLTIPLOS_DOS: {}".format(multiplos_dos))
print("MÚLTIPLOS_TRES: {}".format(multiplos_tres))
print("MÚLTIPLOS_CINCO: {}".format(multiplos_cinco))
print("MÚLTIPLOS_SIETE: {}".format(multiplos_siete))