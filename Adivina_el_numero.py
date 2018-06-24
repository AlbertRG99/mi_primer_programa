numero_a_adivinar = 27

numero_usuario = int(input("Adivina un numero: "))

if numero_usuario == numero_a_adivinar:
    print("Felicidades, has adivinado el número")
else:
    print("Lo siento, has perdido")