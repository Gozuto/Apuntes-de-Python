class pato:
    def hablar(self):
        print("EL pato ha CUAC")
        
class gallina:
    def correr(self):
        print("las gallinas son rapidas")

class humano:
    def atrapar(self, pato):
        pato.hablar(self)
        print("ATRAPADO")
        
Pato = pato()
Humanity = humano()
Humanity.atrapar(pato)                             