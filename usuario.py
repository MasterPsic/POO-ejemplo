class usuario():
    def __init__(self, dni, nombre, apellido, deposito, retiro):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.deposito = deposito
        self.retiro = retiro
        self.saldo = (deposito - retiro)
        self .historial = []

    def listar (self):
        print("""
            Dni; {self.dni}
            Nombre: {self.nombre}
            Deposito: {self.deposito}
            """.format(self.dni, self.nombre, self.deposito))
