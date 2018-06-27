#Simulación de un combate Pokemon hecho por mí, basandome en el modelo de Nate Academy#

pokemon_elegido = input("Elige un Pokemon con el que combatir (Squirtle / Charmander / Bulbasaur): ")

vida_pikachu = 100
vida_contrincante = 0
ataque_contrincante = 0

#Ataques Pikachu#
ataque_bolavoltio = 9
ataque_chispazo = 12


if pokemon_elegido == "Squirtle":
    vida_squirtle = 100
    ataque_squirtle = 10
    ataque_contrincante = ataque_squirtle
    vida_contrincante = vida_squirtle
    print("Has elegido a Squirtle: Vida{}, Ataque{}".format(vida_squirtle, ataque_squirtle))


elif pokemon_elegido == "Charmander":
    vida_charmander = 80
    ataque_charmander = 15
    ataque_contrincante = ataque_charmander
    vida_contrincante = vida_charmander
    print("Has elegido a Charmander: Vida{}, Ataque{}".format(vida_charmander, ataque_charmander))

elif pokemon_elegido == "Bulbasuaur":
    vida_bulbasaur = 90
    ataque_bulbasaur = 17
    ataque_contrincante = ataque_bulbasaur
    vida_contrincante = vida_bulbasaur
    print("Has elegido a Bulbasaur: Vida{}, Ataque{}".format(vida_bulbasaur, ataque_bulbasaur))

while vida_contrincante > 0 and vida_pikachu > 0:
    ataque_elegido = input("Que ataque quieres elegir? (Bola voltio / Chispazo)")

    if ataque_elegido == "Bola voltio":
        vida_contrincante -= ataque_bolavoltio
    elif ataque_elegido == "Chispazo":
        vida_contrincante -= ataque_chispazo
    print("La vida de {} ahora es de {}".format(pokemon_elegido, vida_contrincante))
    vida_pikachu -= ataque_contrincante

    print("La vida de Pikachu ahora es de {}".format(vida_pikachu))


if vida_contrincante >= 0:
    print("Has ganado")
if vida_pikachu <= 0 :
    print("Has perdido")

print("El combate ha terminado")