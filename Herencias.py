class animal:
    vivo = True
    
    def comer(self):
        print("puede comer")
    
    def dormir(self):
        print("puede dormir")
        
class Conejo(animal):
    pass

class Pez(animal):
    def comer(self):
        print("comeprincipalmente plancton")

class Halcon(animal):
    pass


conejo = Conejo()
pez = Pez()
halcon = Halcon()

print(conejo.vivo)
pez.comer()
halcon.dormir()