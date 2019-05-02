import Product.AbstractProductSignificado as APS
import Product.AbstractProductSinonimo as APSN
import Product.AbstractProductAntonimo as APA

class AbstractFactory:
    def Significado(self):
        raise NotImplementedError("Significado() debe ser definido en la subclase")

    def Sinonimo(self):
        raise NotImplementedError("Sinonimo() debe ser definido en la subclase")
    
    def Antonimo(self):
        raise NotImplementedError("Antonimo() debe ser definido en la subclase")

class ConcreteFactoryRAE(AbstractFactory):
    def Significado(self):
        return APS.significadoRAE()
    
    def Sinonimo(self):
        return APSN.sinonimoRAE()

    def Antonimo(self):
        return APA.antonimoRAE()

class ConcreteFactoryWiki(AbstractFactory):
    def Significado(self):
        return APS.significadoWiki()
    
    def Sinonimo(self):
        return APSN.sinonimoWiki()

    def Antonimo(self):
        return APA.antonimoWiki()