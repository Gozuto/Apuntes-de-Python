
class auto:
    ruedas = 4
    def __init__(self,marca,modelo,ano,color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

    def arrancar(self):
        print("Encendiste el motor")
        return self
    
    def condicir(self):
        print("El auto esta en movimiento")
        return self
    
coche = auto()

coche.arrancar().condicir()