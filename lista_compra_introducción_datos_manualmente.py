
mi_lista = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("Qué necesitas comprar? (Escribe FIN para salir)")
    if input_usuario != "FIN":                                                                                          #Usaremos este método para no añada "FIN" a la propia lista cuando lo introducimos#
        mi_lista.append(input_usuario)

largo_lista = len(mi_lista)                                                                                             #En Python podemos saber el largo de una lista usando "Len()"#
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra")