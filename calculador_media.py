"""
Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )
"""
# Programa para demostrar (MEDIA ARITMÉTICA) mean()
# Función para el módulo STATICS

# Importar módulo STATICS
import statistics

# Lista de numeros enteros positivos
lista_usuario = []

while lista_usuario != "00"
    lista_usuario = input("Introduce los números: (Escribe '00' para finalizar)")

x = statistics.mean(lista_usuario)

# Imprimiendo la media
print("Mean is :", x)