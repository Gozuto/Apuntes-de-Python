comida = ['capirotada','Pizza','hambuerguesa'] #declarar
Bebida = ['Limonada','Amper','Refresco']

Menu = [comida, Bebida]

comida[0] ='Helado' #reemplazar
comida.append('Sushi') #agregar al final
comida.remove('Pizza') #Elimiar
comida.pop() #Eliminar ultimo dato
comida.insert(0,'Puddin') #añadir en un lgar en especifico
comida.sort() #ordenar alphabeticamente
#comida.clear() #vaciar lista
print(comida)

c = int(input("que desea comer?"))
b = int(input("que desea tomar?"))
print(Menu[c][b])
print("a la orden señor")



