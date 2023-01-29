class Fecha():
    def __init__(self):
        self.dia = 1
    
    def obtenerdia(self):
        return self.dia

    def dardia(self, dia):
        if dia > 0 and dia <= 31:
            self.dia = dia
        else: 
            print("Error")

#Instanciamos
mi_fecha = Fecha()
print(mi_fecha.obtenerdia())
mi_fecha.dardia(24)
print(mi_fecha.obtenerdia())