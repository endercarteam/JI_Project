import json
import abc
from Fotos import Fotos
from Servicio_Fotografico import Servicio_Fotografico
from Impresion import Impresion
Fotos10x15 = Fotos.Fotos10x15
Fotos13x18 = Fotos.Fotos13x18
Fotos20x25 = Fotos.Fotos20x25
Fotos8 = Servicio_Fotografico.Fotos8
Fotos12 = Servicio_Fotografico.Fotos12
Fotos24 = Servicio_Fotografico.Fotos24
BlancoyNegro = Impresion.BlancoyNegro
Color = Impresion.Color
Pormayor = Impresion.Pormayor
class Gestion_Datos(abc.ABC):
    @abc.abstractclassmethod
    def add_Data(self)->None:
        ...

    @abc.abstractclassmethod
    def show_Data(self)->None:
        ...    


class Pendientes(Gestion_Datos):
    def add_Data(self)-> None:
        print("Digite el nombre del cliente")
        nombre = input()
        print("escoja a continuacion la categoria:\n1.Impresion de Fotos\n2. Servicio Fotografico\n3.Impresion\n4.Fotocopia\n5.Escaneo\n6.Hoja de vida\n7.Edicion de fotos\n8s.Reparacion de fotos")
        Categoria = input()
        if Categoria == 1:
            Cat = "Fotos"
            print("seleccione una de las siguientes opciones:\n1. Foto 10x15cm")

        Pendiente = {"nombre": nombre,"Categoria":Cat}

    def show_Data(self)->None:
        ...     

class Completados(Gestion_Datos):
    def add_Data(self)-> None:
        pass 

    def show_Data(self)->None:
        ...           
