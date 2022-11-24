class Fotos:
    def __init__(self, Tamaño:str, Cantidad:int, Precio:int)->None:
        self.Tamaño: Tamaño
        self.Cantidad: Cantidad
        self.Precio: Precio

    @classmethod
    def Fotos10x15(self,Cant):
        self.Tamaño = "10x15"
        self.Cantidad = Cant
        self.Precio = 15000 
        Costo = self.Cantidad * self.Precio
        return Costo
    @classmethod    
    def Fotos13x18(self, Cant):
        self.Tamaño = "13x18"
        self.Cantidad = Cant
        self.Precio = 16000 
        Costo = self.Cantidad * self.Precio
        return Costo
    @classmethod
    def Fotos20x25(self, Cant):
        self.Tamaño = "20x25"
        self.Cantidad = Cant
        self.Precio = 18000 
        Costo = self.Cantidad * self.Precio
        return Costo
    @classmethod
    def Fotos3x4(self):
        self.Tamaño = "20x25"
        self.Cantidad = 6
        self.Precio = 15000 
        Costo =  self.Precio
        return Costo
