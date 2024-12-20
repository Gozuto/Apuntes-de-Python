
def saludo (**kwargs):
    print("hola", end=" ")
    
    for clave, valor in kwargs.items():
        print(valor, end=" ")

saludo(titulo = "Ingeniero", nombre = "Luis" , apellido = "Aguirre")