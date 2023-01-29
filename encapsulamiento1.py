class Banco:
    def __init__(self):
        self.codigo = 123456
    
    def cuenta(self):
        print("Numero de transacción")
    
    def getcodigo(self):
        return self.codigo

#instanciar
cliente = Banco()
cliente.cuenta
cliente.getcodigo