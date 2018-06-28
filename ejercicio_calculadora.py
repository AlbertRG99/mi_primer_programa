#Crea una calculadora que le pregunte al usuario que quiere hacer, a la vez que dos números con los que operará#

print("Bienvenido a esta calculadora."
      "Podrás trabajar únicamente dos números y una operación")

operacion = input("¿Qué operación quieres realizar? (multiplicar / dividir / sumar / restar)")

primer_numero = int(input("Inserta el primer número"))
segundo_numero = int(input("Inserta el segundo número"))

signo_sumar = "+"
signo_restar = "-"
signo_multiplicar = "*"
signo_dividir = "/"

if operacion == "multiplicar":
    resultado = int(primer_numero*segundo_numero)
    print("Operación definida     {}{}{}".format(primer_numero, signo_multiplicar, segundo_numero))
    print("RESULTADO = {}".format(resultado))

elif operacion == "dividir":
    resultado = primer_numero/segundo_numero
    print("Operación definida     {}{}{}".format(primer_numero, signo_dividir, segundo_numero))
    print("RESULTADO = {}".format(resultado))

elif operacion == "sumar":
    resultado = primer_numero+segundo_numero
    print("Operación definida     {}{}{}".format(primer_numero, signo_sumar, segundo_numero))
    print("RESULTADO = {}".format(resultado))

elif operacion == "restar":
    resultado = primer_numero-segundo_numero
    print("Operación definida     {}{}{}".format(primer_numero, signo_restar, segundo_numero))
    print("RESULTADO = {}".format(resultado))

