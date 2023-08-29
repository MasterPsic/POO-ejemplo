from datos import Ingreso

class Menu():
    def opciones(self):
        ingreso = Ingreso()
        while True:
             print('''
            1 Agregar Producto
            2 Listar
            3 Editar saldo
            4 historial
            5 Consulta de Usuario
            6 Modificar Usuario
            7 Eliminar Usuario
            8 Salir''')
            opcion = int(input(input'Elija una opcion: '))
            if opcion >= 1 and opcion <= 7:
                if opcion == 1:
                    ingreso.agregar()
                elif opcion == 2:
                    ingreso.mostrar()
                elif opcion == 3:
                    ingreso.editarSaldo()
                elif opcion == 4:
                    ingreso.historial()
                elif opcion == 5:
                    ingreso.mostrarUsuario()
                elif opcion == 6:
                    ingreso.editarUsuario()
                elif opcion == 6:
                    ingreso.editarUsuario()
                elif opcion == 7:
                    ingreso.eliminarUsuario()
                elif opcion == 0:
                    ingreso.salir()
            else:
                    print('ingresar una opcion Valida')
                                
menu = Menu()
menu.opciones()
