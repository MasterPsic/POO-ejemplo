from usuario import Usuario
listaUsuario = []
class Ingreso():
    def agregar (self):
        print('agregar Usuario')
        dni = input('Dni:')
        nombre = input('Nombre: ')
        apellido = input('apellido: ')
        deposito = int(input('deposito'))
        retiro = int(input('retiro'))
        objeto = Usuario(dni, nombre, apellido, deposito, retiro)
        listaUsuario.append(objeto)


    def mostrar(self:)
    print('lista de usuarios')
    for obj in listaUsuario:
        obj.listar()
        