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
        print("Digite el nombre del cliente")
        nombre = input()
        print("escoja a continuacion la categoria:\n1.Fotos\n2.Impresion\n3.Fotocopia\n4.Escaneo\n5.Hoja de vida\n6.Edicion de fotos\n7.Reparacion de fotos")
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
