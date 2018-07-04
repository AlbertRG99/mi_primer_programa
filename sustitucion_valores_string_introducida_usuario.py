#Usando el comado '.replace(,)'#
"""
Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.
"""

string_usuario = input("Introduce una frase poara sustituir las 'A' por la palabra 'VACA': ")
string_usuario = string_usuario.upper()
string_usuario = string_usuario.replace("A", "VACA")
string_usuario = string_usuario.lower()

print(string_usuario)