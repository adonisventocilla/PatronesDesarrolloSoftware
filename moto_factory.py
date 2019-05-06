from abc import ABCMeta, abstractstaticmethod


class Imoto(metaclass=ABCMeta): 
    """interface de moto"""

    @abstractstaticmethod
    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._color = color


class Honda(Imoto): 
    """la clase Honda se implementa de Imoto"""
    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 12000
        self._color = color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: MOTO")
        print("MARCA: HONDA")
        movil=f"""color: {self._color} \
            cantidad: {self._cant} unit\
            precio unit: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio tot s/d: {preciot} soles \
        desc: {desc} soles\
        precio tot c/d: {preciof} soles"""
        return precTot


class Hyundai(Imoto): 
    """la clase Hyundai se implementa de Imoto"""

    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 25000
        self._color=color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: MOTO")
        print("MARCA: Hyundai")
        movil=f"""color: {self._color} \
            cantidad: {self._cant} unit\
            precio unit: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio tot s/d: {preciot} soles \
        desc: {desc} soles\
        precio tot c/d: {preciof} soles"""
        return precTot


class Subaru(Imoto):  
    """la clase Subaru se implementa de Imoto"""

    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 22000
        self._color=color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: MOTO")
        print("MARCA: Subaru")
        movil=f"""color: {self._color} \
            cantidad: {self._cant} unit\
            precio unit: {self._prec} soles"""
      
        return movil

    def cotizacion(self):
        print("COTIZACION DE PRODUCTO")
        if self._cant>=4:
            preciot=self._prec*self._cant
            desc=preciot*0.15
            preciof=preciot-desc
        if 0< self._cant<4:
            preciot=self._prec*self._cant
            desc=preciot*0.05
            preciof=preciot-desc
        precTot=f"""precio tot s/d: {preciot} soles \
        desc: {desc} soles\
        precio tot c/d: {preciof} soles"""
        return precTot


class moto_Factory:  
    """Clase fractoria moto"""

    @staticmethod
    def get_marca(tipo):
        
        cant=int(input("ingresa la cantidad a comprar: \
            "))
        col=input("ingresa el color del auto: \
            ")
        try:
            if tipo == "honda":
                return Honda(cant,col)
            if tipo == "hyundai":
                return Hyundai(cant,col)
            if tipo == "subaru":
                return Subaru(cant,col)
            raise AssertionError("marca no encontrada")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    movil=input("ingresa tu movil")
    tipo_vehiculo = moto_Factory.get_marca(movil)
    print(f"MARCA: {movil}")
    print(tipo_vehiculo.descrip_product())
    print(tipo_vehiculo.cotizacion())