salida = False
agenda = []
agenda = [["Jose", "673759575"], ["Maria", "648762402"]]

while not salida:
    accion = input("Qué quieres hacer? Añadir número [A] / Consultar numero [C] / Salir [S]: ")

    #Acción añadir
    if accion == "A":
        print("Vamos a añadir un número de teléfono: ")
        print("--------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda.append([nombre, numero])

    #Acción consultar
    elif accion == "C":
        print("Consultar número: ")
        print("--------------------------------------")
        nombre = input("De quien quieres saber el número: ")
        for nombre_numero in agenda:
            if nombre_numero[0] == nombre:
                print(nombre_numero[1])

    #Acción salir
    elif accion == "S":
        salida = True