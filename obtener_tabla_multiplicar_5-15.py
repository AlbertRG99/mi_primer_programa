"""
Modifica el programa de la tabla de multiplicar para que vaya del 5 al 15 en lugar del 1 al 10.
"""

numero_tabla = int(input("De que número quieres la tabla de multiplicar?: "))

for multiplo in range(5, 16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))