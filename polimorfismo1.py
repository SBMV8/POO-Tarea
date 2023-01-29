class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("El perro ladra")
    
class Caballo(Animal):
    def hablar(self):
        print("El caballo relincha")

#Instanciamos con un bucle for
for animal in Perro(), Caballo():
    animal.hablar()