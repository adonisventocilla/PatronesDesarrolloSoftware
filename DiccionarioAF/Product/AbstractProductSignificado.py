class AbstractProductSignificado:
    def Mostrar(self):
        raise NotImplementedError("Mostrar() debe ser definido en la subclase")

class significadoRAE(AbstractProductSignificado):
    def Mostrar(self):
        print("Dentro de significadoRAE:Mostrar()")

class significadoWiki(AbstractProductSignificado):
    def Mostrar(self):
        print("Dentro de significadoWiki:Mostrar()")