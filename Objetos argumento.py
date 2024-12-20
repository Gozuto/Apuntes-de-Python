class coche:
    color = None

def cambiacolor(vehiculo , color):
    vehiculo.color = color

coche1 = coche()
coche2 = coche()
coche3 = coche()

cambiacolor(coche1, "rojo")
cambiacolor(coche2, "azul")
cambiacolor(coche3, "verde")

print(coche1.color)
print(coche2.color)
print(coche3.color)