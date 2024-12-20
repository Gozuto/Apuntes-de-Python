import random

jugador = input("Elije, favor de escribir en minusculas\n")

JanKenPo = ["piedra" , "papel" , "tijeras"]
IA = random.choice(JanKenPo)

print("Elegiste: " + jugador + "\nYo elegi: " + IA)

if IA != jugador:
    if IA == "piedra" and jugador == "papel" or IA == "papel" and jugador == "tijeras" or IA == "tijeras" and jugador == "piedra":
        print("Ganaste")
    else:
        print("Perdise")
else:
    print("Empate")