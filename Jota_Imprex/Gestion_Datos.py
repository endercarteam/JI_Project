import json
import abc
class Gestion_Datos(abc.ABC):
    @abc.abstractclassmethod
    def actualizar(self)->None:
        ...


class Pendientes(Gestion_Datos):
    def actualizar(self)-> None:
        pass

class Completados(Gestion_Datos):
    def actualizar(self)-> None:
        pass           
