from abc import ABC, abstractmethod

class Mate(ABC):
    @abstractmethod
    def Area(self):
        pass
    def Perimetro(self):
        pass

class Cuadrado(Mate):
    def __init__(self, lado):
        self.lado = lado
    
    def Area(self):
        return self.lado*self.lado

    def Perimetro(self):
        return self.lado*4

#instanciamos el cuadrado
c1 = Cuadrado(8)

print("El area del cuadrado es:",c1.Area())
print("El perimetro del cuadrado es:",c1.Perimetro())