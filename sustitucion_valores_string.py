"""
Crea un código que, utilizando el método "replace" de las strings, me sustituya las claves de mi string inicial por los valores en orden de una lista
"""

valores_a_sustituir = [1, 2, "hola", "adios"]
string_a_cambiar = "Hola, número {}, numero {}, {} y {}"

"Hola, número 1, número 2, hola y adiós"

for valor in valores_a_sustituir:
    string_a_cambiar = string_a_cambiar.replace("{}", str(valor), 1)      #Esto significa que cambiamos el corchete por el valor pero de 1 en 1#
                                                                          #También podemos camiar el tipo de elemento con str.(valor)#
print(string_a_cambiar)