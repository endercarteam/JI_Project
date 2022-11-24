class Fotocopias:
    def __init__(self, Cantidad=int, Tipo=str, Precio=int) -> None:
        self.Cantidad = Cantidad
        self.Tipo=Tipo
        self.Precio = Precio
    @classmethod
    def BlancoyNegro(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Blanco y Negro"
        self.Precio = 200
        ToT = self.Cantidad * self.Precio
        return ToT
    @classmethod
    def Color(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Color"
        self.Precio = 400
        ToT = self.Cantidad * self.Precio
        return ToT
    @classmethod
    def Pormayor(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Fotocopias al por mayor"
        self.Precio = 80
        ToT = self.Cantidad * self.Precio
        return ToT    
