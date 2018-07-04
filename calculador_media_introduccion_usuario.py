"""
Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )
"""

number_list = []
loop_finalized = False

while loop_finalized == False:
    nunber = input("Que numero quieres introducir")
    if not nunber == "fin":
        number_list.append(int(nunber))
    else:
        loop_finalized = True

list_len = len(number_list)

total = 0
for i in number_list:
    total += i

result = total / list_len

print("La media de {} es {}".format(number_list, result))