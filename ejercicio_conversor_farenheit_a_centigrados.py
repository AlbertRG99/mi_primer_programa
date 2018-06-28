#Transformar de grados Farenheit a Centigrados [Celsius = (Farenheit - 32) * (5/9)], mostrando el resultado formateado en una estring usando el .format#

print("Bienvenido al conversor Farenheit - Celsius")
valor = int(input("Introduce un valor en Uds.Farenheit: "))

resultado = int(((valor-32)*5)/9)

print("{} G.Farenheit son {} G.Celsius".format(valor, resultado))