class Impresion:
    def __init__(self, Cantidad=int, Tipo=str, Precio=int):
        self.Cantidad = Cantidad
        self.Tipo=str
        self.Precio = int

    def BlancoyNegro(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Blanco y Negro"
        self.Precio = 600
        ToT = self.Cantidad * self.Precio
        return ToT

    def Color(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Color"
        self.Precio = 1200
        ToT = self.Cantidad * self.Precio
        return ToT

    def Pormayor(self, Cantidad):
        self.Cantidad = Cantidad
        self.Tipo= "Fotos al por mayor"
        self.Precio = 80
        ToT = self.Cantidad * self.Precio
        return ToT
