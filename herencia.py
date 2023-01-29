class Perro:
    def __init__(self, raza, edad):
        self.raza = raza
        self.edad = edad
    
    def hablar(self):
        print("Guau!")
    
    def moverse(self):
        print("Camina en 4 patas")

    def getInfo(self):
        return f"""Raza: {self.raza}\nEdad: {self.edad}"""

#instanciamos al perro
mi_perro = Perro("Cocker Spaneil Ingles", "6 meses")

print(mi_perro.getInfo())
mi_perro.hablar()
mi_perro.moverse()