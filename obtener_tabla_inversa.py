"""
Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario, pero invertida, comenzando desde el 10.
"""


numero_usuario = int(input("¿Qué número quieres multiplicar?: "))


for multiplicardor in range(10, 0, -1):
    print("{} x {} = {}".format(numero_usuario, multiplicardor,  numero_usuario * multiplicardor))

