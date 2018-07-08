def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, Estás seguro? [Si/No] ".format(dato_usuario))
        if seguro == "Si":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("Cómo te llamas?")
print("Has confirmado que te llamas {}".format(nombre))

numero = input_con_confirmacion("Dime un número ")
print("Has confirmado que el numero es {}".format(numero))
