from abc import ABC, abstractmethod

class vehiculo(ABC):
    @abstractmethod
    def ir(self):
       pass
   
class coche(vehiculo):
    def ir(self):
       print("Estas usando un carro")

class moto(vehiculo):
    def ir(self):
       print("Estas usando una moto")   
       
Carro = coche()
Moto = moto()
Moto.ir()
