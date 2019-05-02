class AbstractProductAntonimo:
    def Mostrar(self):
        raise NotImplementedError("Mostrar() debe ser definido en la subclase")

class antonimoRAE(AbstractProductAntonimo):
    def Mostrar(self):
        print("Dentro de antonimoRAE:Mostrar()")

class antonimoWiki(AbstractProductAntonimo):
    def Mostrar(self):
        print("Dentro de antonimoWiki:Mostrar()")