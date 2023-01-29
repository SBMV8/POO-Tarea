class Abeja:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def hablar(self):
        print("Bzzz!")
    
    def moverse(self):
        print("volando")

    def picar(self):
        print("Picar!")

    def getInfo(self):
        return f"""Tipo: {self.tipo}"""

#instanciamos a la Abeja
mi_abeja = Abeja("Abeja Reina")

print(mi_abeja.getInfo())
mi_abeja.hablar()
mi_abeja.moverse()
mi_abeja.picar()