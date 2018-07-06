"""
Dada una lista de enteros:
Vamos a sustituir los múltiplos de 3 por un Fizz
y los múltiplos de 5 por un Buzz
múltiplos de 3 y 5, vamos a sustituirlos por un FizzBuzz
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""

        if numero % 3 == 0:
            numeros[indice] += "Fizz"           #Le añado el Fizz a la variable numeros[indice]#

        if numero % 5 == 0:                     #Le añado el Buzz a la variable numeros[indice]#
            numeros[indice] += "Buzz"

print(numeros)