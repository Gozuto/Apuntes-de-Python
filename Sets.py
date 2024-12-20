#Sets son como listas, pero no permiten elementos duplicados

DarkRebellion = {"Dark Rebellion XYZ Dragon", 4 , 2500, 2000, "Roba mitad de ataque"}
DarkRequiem = {"Dark Requiem XYZ Dragon", 5 , 3000, 2500, "Roba Todo el ataque"}

DarkRebellion.update(DarkRequiem) #añade los datos de Requiem a Rebellion
print(DarkRebellion.difference(DarkRequiem)) #Muestra los datos que tiene Rebellion, pero no Requiem
print(DarkRebellion.intersection(DarkRequiem)) #Muestra los datos que tienen ambos en comun
for x in DarkRebellion:
    print(x) #lo va a imprimir, aunque en desorden


