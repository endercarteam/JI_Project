class Servicio_Fotografico:
    def __init__(self, Cantidad=int, Precio=int):
        self.Cantidad = Cantidad
        self.Precio = Precio

    def Fotos8(self):
        self.Cantidad = 8
        self.Precio = 55000
        return self.Precio

    def Fotos12(self):
        self.Cantidad = 12
        self.Precio = 80000
        return self.Precio 

    def Fotos24(self):       
        self.Cantidad = 24
        self.Precio = 125000
        return self.Precio
