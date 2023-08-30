from vehiculo import Vehiculo
class Moto(Vehiculo):
    def __init__(self, Marca, Modelo, Color, patente):
        super().__init__(Marca, Modelo, Color)
        self.patente = patente

    def __str__(self):
        return super().__str__() + f"""
                La patente es: {self.patente}
        """
    