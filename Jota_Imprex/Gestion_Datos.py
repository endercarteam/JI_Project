import json
import abc
from Fotos import Fotos
from Servicio_Fotografico import Servicio_Fotografico
from Impresion import Impresion
from Edicion import Edicion
from Fotocopias import Fotocopias
Archivo_Pendientes = "PPendientes.json"
Archivo_Completados = "PCompletados.json"



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
            print("seleccione una de las siguientes opciones:\n1. Foto 10x15cm\n2. Fotos 13x18\n3. Fotos 20x25\n4. Fotos2x4")
            F = int(input())
            if F == 1:
                Tipo= str("Tamaño 10x15")
                print("Digite la cantidad de Fotos que requiere")
                Cant = int(input())
                Price = Fotos.Fotos10x15(Cant)
                print (F"El precio a pagar es: ", Price)
            else: 
                if F ==2:
                    Tipo = str("Tamaño 13x18")
                    print("Digite la cantidad de Fotos que requiere")
                    Cant = int(input())
                    Price = Fotos.Fotos13x18(Cant)
                    print (F"El precio a pagar es: ", Price)
                else: 
                    if F == 3:
                        Tipo= str("Tamaño 20x25")
                        print("Digite la cantidad de Fotos que requiere")
                        Cant = int(input())
                        Price = Fotos.Fotos20x25(Cant)
                        print (F"El precio a pagar es: ", Price)
                    else:
                        if F==4:
                            Tipo= str("Tamaño 3x4")
                            
                            Cant = 6
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
                    Cant = 8
                    print(f"El precio a pagar es: ", Price)     

                else:
                    if F == 2:
                        Tipo = str("12 Fotos")
                        Price = Servicio_Fotografico.Fotos12()
                        Cant = 12
                        print(f"El precio a pagar es: ", Price)
                    else:
                        if F ==3:    
                            Tipo = str("24 Fotos")
                            Cant = 24
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
                    if Categoria == 4: 
                        Cat = str("Fotocopias")
                        print("seleccione una de las siguientes opciones: \n1. Blanco y negro\n2. Color\n3. Al por mayor(Mas de 400 fotocopias)")  
                        F = int(input())
                        if F == 1:
                            Tipo = str("Fotocopia a blanco y negro")
                            print("Por favor ingrese a continuacion la cantidad de impresiones que necesita: ")
                            Cant = int(input())
                            Price = Fotocopias.BlancoyNegro(Cant)
                            print(f"El precio a pagar por sus fotocopias es: ", Price)
                        else:
                            if F == 2:
                                Tipo = str("Fotocopia a blanco y negro")
                                print("Por favor ingrese a continuacion la cantidad de impresiones que necesita: ")
                                Cant = int(input())
                                Price = Fotocopias.BlancoyNegro(Cant)
                                print(f"El precio a pagar por sus fotocopias es: ", Price)
                            else:
                                if F ==3:
                                    Tipo = str("Fotocopias al por mayor")
                                    print("Por favor ingrese a continuacion la cantidad de impresiones que necesita: ")
                                    Cant = int(input())
                                    Price = Fotocopias.Pormayor(Cant)
                                    print(f"El precio a pagar por sus fotocopias es: ", Price)    
                    else:
                        if Categoria == 5:
                            Cat = str("Edicion y Reparacion")
                            print("seleccione una de las siguientes opciones: \n1. Edicion \n2. Reparacion")    
                            F = int(input())
                            if F == 1:
                                Tipo = str("Edicion Normal")
                                print("Por favor ingrese a continuacion la cantidad de fotos a editar: ")
                                Cant = int(input())
                                Price = Edicion.EN(Cant)
                                print(f"El precio a pagar es: ", Price) 
                            else:
                                if F == 2:
                                    ipo = str("Edicion Normal")
                                print("Por favor ingrese a continuacion la cantidad de fotos a restaurar: ")
                                Cant = int(input())
                                Price = Edicion.EN(Cant)
                                print(f"El precio a pagar es: ", Price)             




        Pendiente = {"nombre": str(nombre),"Categoria":str(Cat),"Tipo": str(Tipo), "Cantidad": int(Cant), "Precio": (Price)}
        
        
        with open(Archivo_Pendientes, "r+") as file:
            data = json.load(file)
            data.append(Pendiente)    
            file.seek(0)
            json.dump(data,file)

    def show_Data(self)->None:
      with open(Archivo_Pendientes, "r") as file:
            data = json.load(file) 
            print (data)        
class Completados(Gestion_Datos):
    def add_Data(self)-> None:
        
        print ("Digite el diccionario que quiere pasar a la lista de Completados:")
        Pass_to = str(input())

        with open(Archivo_Completados, "r+") as file:
            data = json.load(file)
            data.append(Pass_to)    
            file.seek(0)
            json.dump(data,file)
    

    def show_Data(self)->None:
        with open(Archivo_Completados, "r") as file:
            data = json.load(file) 
            print (data)
