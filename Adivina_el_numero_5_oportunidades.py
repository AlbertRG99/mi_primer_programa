numero_a_adivinar = 27

counter = 0

label: ejecucion

numero_usuario = int(input("Adivina un numero: "))

if numero_usuario == numero_a_adivinar:
    print("Felicidades, has adivinado el número")
else:
    print("Lo siento, has perdido")

counter = counter + 1
while counter < 5:
    goto final

goto ejecucion

label: final
print (¨Has superado el número máximo de veces permitidas¨)