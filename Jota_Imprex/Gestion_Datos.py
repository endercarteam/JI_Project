import json
import abc
from Fotos import Fotos
from Servicio_Fotografico import Servicio_Fotografico
from Impresion import Impresion
from Edicion import Edicion
from Fotocopias import Fotocopias


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
        nombre = str(input())
        print("escoja a continuacion la categoria:\n1.Impresion de Fotos\n2. Servicio Fotografico\n3.Impresion\n4.Fotocopia\n5.Edicion de fotos o Reparacion de fotos")
        Categoria = int(input())
        if Categoria == 1:
            Cat = str("Fotos")
            print("seleccione una de las siguientes opciones:\n1. Foto 10x15cm\n2. Fotos 13x18\n3. Fotos 20x25")
            F = int(input())
            if F == 1:
                Tipo: str("Tamaño 10x15")
                print("Digite la cantidad de Fotos que requiere")
                Cant = int(input())
                Price = Fotos.Fotos10x15(Cant)
                print (F"El precio a pagar es: ", Price)
            else: 
                if F ==2:
                    Tipo: str("Tamaño 13x18")
                    print("Digite la cantidad de Fotos que requiere")
                    Cant = int(input())
                    Price = Fotos.Fotos13x18(Cant)
                    print (F"El precio a pagar es: ", Price)
                else: 
                    if F == 3:
                        Tipo: str("Tamaño 20x25")
                        print("Digite la cantidad de Fotos que requiere")
                        Cant = int(input())
                        Price = Fotos.Fotos20x25(Cant)
                        print (F"El precio a pagar es: ", Price)
        else: 
            if Categoria == 2:
                Cat = str("Servicio Fotografico")
                print("seleccione una de las siguientes opciones:\n1. 8 Fotos \n2. 12 Fotos \n3. 24 Fotos")
                F = int(input())
                if F ==1:
                    Tipo = str("8 Fotos")
                    Price = Servicio_Fotografico.Fotos8()
                    print(f"El precio a pagar es: ", Price)     

                else:
                    if F == 2:
                        Tipo = str("12 Fotos")
                        Price = Servicio_Fotografico.Fotos12()
                        print(f"El precio a pagar es: ", Price)
                    else:
                        if F ==3:    
                            Tipo = str("24 Fotos")
                            Price = Servicio_Fotografico.Fotos24()
                            print(f"El precio a pagar es: ", Price)
            else:
                if Categoria == 3:
                    Cat = str("Impresion")
                    print("seleccione una de las siguientes opciones: \n1. Blanco y negro\n2. Color\n3. Al por mayor(Mas de 400 impresiones)")  
                    F = int(input())
                    if F == 1:
                        Tipo = str("Impresion a blanco y negro")
                        print("Por favor ingrese a continuacion la cantidad de impresiones que necesita: ")
                        Cant = int(input())
                        Price = Impresion.BlancoyNegro(Cant)
                        print(f"El precio a pagar por sus impresiones es: ", Price)
                    else:
                        if F==2:
                            Tipo = str("Impresion a color")
                            print("Por favor ingrese a continuacion la cantidad de impresiones que necesita: ")
                            Cant = int(input())
                            Price = Impresion.Color(Cant)
                            print(f"El precio a pagar por sus impresiones es: ", Price)        
                         
                            
                else:
                    Categoria == 4:                     

        Pendiente = {"nombre": nombre,"Categoria":Cat,"Tipo": Tipo, "Cantidad": Cant, "Precio": Price}

    def show_Data(self)->None:
        ...     

class Completados(Gestion_Datos):
    def add_Data(self)-> None:
        pass 

    def show_Data(self)->None:
        ...           
