
def suma (*cosas):
    suma = 0
    cosas = list(cosas)
    #cosas[0] = 0
    for i in cosas:
        suma += i
    return suma

print(suma(6,14,2))
