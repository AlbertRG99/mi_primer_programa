def solo_numeros_pares(lista):
    lista_pares = []
    for numero in lista:
        resto = numero % 2
        if int(resto) == 0:
            numero+= lista_pares
    return lista_pares

FIN = False
lista = []
while FIN is False:
    lista_usuario = input("Introduce los números que quieres compribar (Escribe 'FIN' para continuar0: )")
    lista +=  lista_usuario
    if lista_usuario = "FIN":
        FIN = True

print("La lista de números pares es: {}".format(solo_numeros_pares(lista)))