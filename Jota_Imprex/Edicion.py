class Edicion:
    def __init__(self, Tipo:str, Cantidad:int, Precio:int):
        self.Tipo = Tipo
        self.Cantidad = Cantidad
        self.Precio = Precio
    @classmethod
    def EN(self, Cantidad):
        self.Tipo = "Edicion Normal"
        self.Cantidad = Cantidad
        self.Precio = 8000
        Tot = self.Cantidad * self.Precio
        return Tot
    @classmethod
    def Reparacion(self, Cantidad):
        self.Tipo = "Reparacion de Fotos"
        self.Cantidad = Cantidad
        self.Precio = 12000
        Tot = self.Cantidad * self.Precio
        return Tot        
