"""
Dada una lista de strings, devolver una lista con el largo de cada string.
"""

lista_strings = ["Hola", "me", "llamo", "Jose", "Alberto"]
lista_largo_strings = []

for elemento in lista_strings:
    lista_largo_strings.append(len(elemento))

print(lista_largo_strings)