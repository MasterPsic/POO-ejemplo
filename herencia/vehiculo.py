class Vehiculo():
    def __init__(self, Marca, Modelo, Color):
        self.marca = Marca
        self.modelo = Modelo
        self.color = Color

    def __str__(self):
        return f"""
            Marca: {self.marca}
            Modelo: {self.modelo}:
            Color: {self.color}"""
    