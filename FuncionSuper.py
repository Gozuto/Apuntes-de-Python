class rectangulo:
    def __init__(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
    def area(self):
        return self.largo * self.ancho
    
class cuadrado:
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado
        
class cubo(rectangulo):
    def __init__(self, largo, ancho, alto):
        self.alto = alto
        super().__init__(largo,ancho)
    def volumen(self):
        return self.alto * self.largo * self.ancho

rec1 = rectangulo(3, 3)
cubo1 = cubo(3,3,3)
print(rec1.area())
print(cubo1.volumen())
        

