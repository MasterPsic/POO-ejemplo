from datos import Ingreso
class Menu():
        def opciones(self):
                ingreso = Ingreso()
                while True:
                print('''
                1 Agregar
                2 Listar
                3 Editar saldo
                4 historial
                5 Buscar''')
                opcion = int(input(input'Elija una opcion :'))
                if opcion >= 1 and opcion < 5:
                        if opcion == 1:
                                ingreso.agregar()
                        elif opcion == 2:
                                ingreso.mostrar()
                        elif opcion == 3:
                                ingreso.editarSaldo()
                        elif opcion == 4:
                                ingreso.historial()
                                
menu = Menu()
menu.opciones()
