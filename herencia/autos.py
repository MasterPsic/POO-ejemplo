class Vehiculo():
    def __init__(self, Marca, Modelo, Color):
        self.marca = Marca
        self.modelo = Modelo
        self.color = Color

    def __str__(self):
        return f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        Color: {self.color}'''

class Auto(Vehiculo):
    def __init__(self, Marca, Modelo, Color, puerta,patente):
       super().__init__(Marca, Modelo, Color)
       self.puerta = puerta
       self.patente = patente

    def __str__(self):
        return super().__str__() + f'''
        Cantidad de puertas: {self.puerta}
        La patente del auto es: {self.patente}
            '''
auto = Auto('ford', 'fiesta', 'negro', 4, 'JMH789')
print(auto)
