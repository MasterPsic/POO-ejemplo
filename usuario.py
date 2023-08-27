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
            Retiro: {}
            """.format(self.dni, self.nombre, self.deposito))

    def modificaciones (self, deposito, retiro):
        return f'''
                Deposito: (deposito)
                Retiro: (retiro)
                '''

    def editarSaldo(self, deposito, retiro):
        self.deposito += deposito
        self.retiro +- retiro
        self.saldo += (deposito-retiro):
        
    def editarUsuario(self, nombre, apellido, deposito, retiro):
        self.nombre = nombre
        self.apellido = apellido
        def.deposito = deposito
        def.saldo = +- (deposito-retiro)
