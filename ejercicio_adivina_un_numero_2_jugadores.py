#Adivina un número. Primero le preguntamos al usuario que número va a adivinar. Luego otro ususrio tiene que adivinarlo. El progrma solo terminará si adivina el número#
#En este caso voy a introducir personalmente el comando "time.sleep(segundos)", que nos permitirá pausar el programa#

import time #lo primero que voy a hacer es importar la libreria de tiempo de Python.com#

print("Busca a un compañero y trata de adivinar su numero")

comenzar = input("¿Listos? (si / no)")

while comenzar == "si":
    numero_a_adivinar = int(input("Introduce un número para que sea adivinado por tu compañero (Procura que no lo vea)"))
    print("-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-"
          "-")
    print("De acuerdo, ahora le toca a tu compañero")
    time.sleep(2)

    numero_companero = int(input("COMPAÑERO: Adivina el número"))


    while numero_a_adivinar != numero_companero:
        numero_companero = int(input("Inténtalo otra vez"))

        if numero_a_adivinar == numero_companero:
            print("Felicidades, has adivinado el número")

