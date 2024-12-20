nombre=""

while True:
    nombre=input("cual estu nombre?\n")
    if nombre != "":
        break #Salir / romper la funcion actual y pasar a la siguiente linea de codigo
    
telefono = "123-434-1427"
for i in telefono:
    if i == "-":
        continue #Return
        
    print(i,end="")

for i in range(1,20):
    if i == 13:
        pass  #El programa usra todo su poder para que la funcion absolutamente nada
    else:
        print(i)


