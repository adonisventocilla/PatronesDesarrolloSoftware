class AbstractProductSinonimo:
    def Mostrar(self):
        raise NotImplementedError("Mostrar() debe ser definido en la subclase")

class sinonimoRAE(AbstractProductSinonimo):
    def Mostrar(self):
        print("Dentro de sinonimoRAE:Mostrar()")

class sinonimoWiki(AbstractProductSinonimo):
    def Mostrar(self):
        print("Dentro de sinonimoWiki:Mostrar()")