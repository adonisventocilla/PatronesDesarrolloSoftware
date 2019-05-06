

from abc import ABCMeta, abstractstaticmethod


class Iauto(metaclass=ABCMeta): 
    """interface de auto"""

    @abstractstaticmethod
    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._color=color


class Honda(Iauto): 
    """la clase Honda se implementa de Iauto"""
    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 52000
        self._color = color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")  
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


class Hyundai(Iauto): 
    """la clase Hyundai se implementa de Iauto"""

    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 48000
        self._color = color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")
        print("MARCA: HYUNDAI")   
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


class Subaru(Iauto):  
    """la clase Subaru se implementa de Iauto"""

    def __init__(self,cantidad,color):
        self._cant =cantidad
        self._prec = 35000
        self._color = color
        

    def descrip_product(self):
        print("DESCRIPCCION DE PRODUCTO: AUTO")
        print("MARCA: SUBARU")   
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


class auto_Factory:  
    """clase factoria"""

    @staticmethod
    def get_marca(tipo):
        """A static method to get a table"""
        cant=int(input("ingresa la cantidad a comprar: \
            "))
        col=input("ingresa el color de tu auto: \
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
    tipo_vehiculo = auto_Factory.get_marca(movil)
    print(f"MARCA: {movil}")
    print(tipo_vehiculo.descrip_product())
    print(tipo_vehiculo.cotizacion())