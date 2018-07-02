"""
Crea un programa que encuentre el número más pequeño de una serie de números introducidos por el usuario.
"""

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():                                                         #FUNCIÓN .isdigit()#
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

numero_pequeno = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El número más pequeño es {}".format(numero_pequeno))
