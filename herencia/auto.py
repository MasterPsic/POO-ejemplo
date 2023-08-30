from vehiculo import Vehiculo
class Auto(Vehiculo):
    def __init__(self, Marca, Modelo, Color, velocidad, puerta, patente):
        super().__init__(Marca, Modelo, Color, velocidad)
        self.puerta = puerta
        self.patente = patente

    def __str__(self):
        return super().__str__() + f"""
                Cantidad de puertas: {self.puerta}
                La patente del auto es: {self.patente}"""
    