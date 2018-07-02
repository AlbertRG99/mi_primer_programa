"""
Pregunta al usuario una serie de 10 números. Después obtén el mayor de ellos.
"""

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():                                                         #FUNCIÓN .isdigit()#
        numero_del_usuario = input("Dime un numero: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("Número añadido")

numero_grande = numeros_usuario[0]

for numero in numeros_usuario:
    if numero > numero_grande:
        numero_grande = numero

print("El número más grande es {}".format(numero_grande))
