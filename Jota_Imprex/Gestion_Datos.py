import json
import abc
class Gestion_Datos(abc.ABC):
    @abc.abstractclassmethod
    def add_Data(self)->None:
        ...

    @abc.abstractclassmethod
    def show_Data(self)->None:
        ...    


class Pendientes(Gestion_Datos):
    def add_Data(self)-> None:

        Pendiente = {}

    def show_Data(self)->None:
        ...     

class Completados(Gestion_Datos):
    def add_Data(self)-> None:
        pass 

    def show_Data(self)->None:
        ...     
