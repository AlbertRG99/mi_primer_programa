"""
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).

numero_en_rango(10, 1, 100) # Devuelve True
numero_en_rango(101, 1, 100) # Devuelve False
"""

def comprobacion_rango(num, num_inicio, num_final):
    comprobacion = ""
    if num in range(num_inicio, num_final):
        comprobacion = "True"
    else:
        comprobacion = "False"
    return comprobacion

num = int(input("Introduce el número a comprobar: "))
num_inicio = int(input("Introduce el primer número del rango: "))
num_final = int(input("Introduce el segundo número del rango"))

print(comprobacion_rango(num, num_inicio, num_final))