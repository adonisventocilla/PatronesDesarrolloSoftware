
from abc import ABCMeta, abstractstaticmethod
from auto_factory import auto_Factory
from moto_factory import moto_Factory


class IVehiculoFactory(metaclass=ABCMeta):
    """interface vehiculo factory"""

    @abstractstaticmethod
    def get_vehiculo(tipo):
        """metodo static de vehiculo factory"""


class VehiculoFactory(IVehiculoFactory): 
    """clase vehiculofactory"""

    @staticmethod
    def get_vehiculo(tipo):
        """Static get_furniture method"""
        try:
            if tipo=="auto":
                movil=input("ingresa la marca (honda/hyundai/subaru):\
                    ")
                return auto_Factory().get_marca(movil)
            if tipo=="moto":
                movil=input("ingresa la marca (honda/hyundai/subaru):\
                    ")
                return moto_Factory().get_marca(movil)
            raise AssertionError("factoria vehiculo no encontrada")
        except AssertionError as _e:
            print(_e)
        return None

if __name__ == "__main__":
    movil=input("ingresa el tipo de vehiculo a comprar (auto/moto): \
        ")
    FURNITURE = VehiculoFactory.get_vehiculo(movil)
    print(FURNITURE.descrip_product())
    print(FURNITURE.cotizacion())
