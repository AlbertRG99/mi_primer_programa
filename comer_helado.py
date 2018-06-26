apetece_helado_input = input("Te apetece un helaado? (SI/NO): ")
tiene_dinero_input = input("Tienes dinero para un helado? (SI/NO): ")
esta_el_senor_helados_input = input("Está el señor de los helados? (SI/NO): ")
esta_su_tia_input = input("Estás con tu tia? (SI/NO): ")

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_su_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
