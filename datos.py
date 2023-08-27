from usuario import Usuario
listaUsuario = []

class Ingreso():
    def agregar (self):
        print('Agregar Usuario')
        dniCorrecto = False
        while not dniCorrecto:
            dni = input('Dni:')
            if len(dni) == 8:
                if dni.isnumeric():
                    dniCorrecto = True
                else: 
                    print('Debe contener solo numeros')
            else: 
                print('Dni invalido, debe contener 8 digitos')
        nombreCorrecto = False
        while not nombreCorrecto:
            nombre = input('nombre: ').title()
            if len(nombre) > 2:
                if len(nombre) <= 12:
                    if nombre.isalpha():
                        nombreCorrecto = True
                        print(nombre)
                    else:
                else:
            else:
 # Verificar los ultimos else                       

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

    def mostrarUsuario(self):
        print('consulta de usuario')
        dni: input('ingresa el DNI del usuario')
        for obj in listarUsuario:
            if dni == obj.dni:
                obj,listar()

    def historial(self):
        print ('historial de usuario')
        dni = input('dni: ')
        for obj in listaUsuario:
            if dni == obj.dni:
                for mensaje in obj.historial:
                    print(f'Historial: {mensaje} ')
        
    def editarSaldo(self):
        print('editar saldo')
        dni = input('Dni A editar')
        for usuario in listarUsuario:
            if dni == usuario.dni:
            deposito = int(input('Deposito'))
            retiro == int(input('Retiro'))
            usuario.editarSaldo(deposito, retiro)
            usuario.imprimir()
            modificado =usuario.modificaciones(deposito, retiro)
            usuario.historial.append(modificado)

    def editarUsuario(self):
        print('Editar Saldo')
        dni = input('Ingrese dni a editar')
        for usuario in listarUsuario:
            if dni == usuario.dni:
                nombre = input('Nombre: ')
                apellido = input('Apellido')
                deposito = int(input'Deposito'))
                usuario.editarUsuario(nombre, apellido, deposito, retiro)
                usuario.listar()
                modificado = usuario.modificaciones(deposito, retiro)
                usuario.historial.append(modificado)

    def eliminarUsuario(self)
        print('Eliminar Usuario')
        dni = input('Ingrese dni a Editar')
        for obj in listaUsuario:
            if dni == obj.dni:
                listaUsuario.remove(obj)

    def salir(self):
        print('Fin del Programa')
        exit()
        
        