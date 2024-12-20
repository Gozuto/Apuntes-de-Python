import random
x = random.randint(0,7)
#print(x)
Material = "Error"
RespuestaCorrecta = "Error"


if x == 0:
    Material = "Transistor"
    RespuestaCorrecta = "Transistor"
    respuesta = input("Como se dice " + Material + " en ingles\n")

if x == 1:
    Material = "Cable"
    RespuestaCorrecta = "Wire"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 2:
    Material = "pinzas"
    RespuestaCorrecta = "Pliers"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 3:
    Material = "Alambre de Cobre"
    RespuestaCorrecta = "Cooper Wire"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 4:
    Material = "bobina"
    RespuestaCorrecta = "Coil"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 5:
    Material = "Estano"
    RespuestaCorrecta = "Tin"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 6:
    Material = "Interruptor"
    RespuestaCorrecta = "Switch"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 7:
    Material = "Cautin"
    RespuestaCorrecta = "Soldering Iron"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 8:
    Material = "Cautin"
    RespuestaCorrecta = "Soldering Iron"
    respuesta = input("Como se dice " + Material + " en ingles\n")
    
if x == 9:
    Material = "Cautin"
    RespuestaCorrecta = "Soldering Iron"
    respuesta = input("Como se dice " + Material + " en ingles\n")
if x == 10:
    Material = "Cautin"
    RespuestaCorrecta = "Soldering Iron"
    respuesta = input("Como se dice " + Material + " en ingles\n")



if respuesta == RespuestaCorrecta:
    print("CORRECTO")
else:
    print("Incorrecto")