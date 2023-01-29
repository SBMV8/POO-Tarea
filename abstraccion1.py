from abc import ABC, abstractmethod

class Mate(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Perimetro(self):
        pass

class Circulo(Mate):
    def __init__(self, radio):
        self.radio = radio
    
    def Area(self):
        return self.radio*self.radio*3.1416
    
    def Perimetro(self):
        return self.radio*3.1416*2

#Instanciamos el circulo
c1 = Circulo(12)

print("El area del circulo es:",c1.Area())
print("EL perimetro del circulo es:",c1.Perimetro())