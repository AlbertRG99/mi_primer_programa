"""
Modifica el programa de la tabla de multiplicar para que solo muestre los resultados cuando son multiplos de 2.
"""

numero_tabla = int(input("De que número quieres la tabla de multiplicar? (SOLO MÚLTIPLOS DE 2): "))

for multiplo in range(1, 11):
    resto = multiplo % 2
    if resto == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))