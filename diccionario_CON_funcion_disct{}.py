salida = False
agenda = dict()

while not salida:
    accion = input("Qué quieres hacer? Añadir número [A] / Consultar numero [C] / Salir [S]: ")

    #Acción añadir
    if accion == "A":
        print("Vamos a añadir un número de teléfono: ")
        print("--------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda[nombre] = numero

    #Acción consultar
    elif accion == "C":
        print("Consultar número: ")
        print("--------------------------------------")
        nombre = input("De quien quieres saber el número: ")
        print(agenda[nombre])
    #Acción salir
    elif accion == "S":
        salida = True