"""
Obtener los tipos de datos que hay en una lista introducida por el usuario
"""

#[1, 2, "a", 24, 2.1, False] / Quiero que me retorne una lista pero con los tipos de variables#

lista_datos = [1, 2, 3, "asd", [], True, 23, 2.1]

lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)

