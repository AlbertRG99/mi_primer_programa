'''
Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario.
'''

#En este caso usaremos las funcioes DEF y RETURN para hacer que funcione el programa ya que no encontré otra forma posible#


def mayusculas(cadena: str):

    mayusculas = 0
    
    for letra in cadena:
        if letra == letra.upper() and letra.upper() != letra.lower():
            mayusculas += 1
    
    return mayusculas


cadena = input("Introduce una cadena o letra: ")
numero = mayusculas(cadena)
print(f"Mayusculas: {numero}")
