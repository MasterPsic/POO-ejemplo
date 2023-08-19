from datos import Ingreso
class Menu():
        def opciones(self):
                ingreso = Ingreso()
                while True:
                print('''
                1 Agregar
                2 Listar''')
                opcion = int(input(input'Elija una opcion :'))
                if opcion >= 1 and opcion < 5:
                        if opcion == 1:
                                ingreso.agregar()
                        elif opcion == 2:
                                ingresar.mostrar()
                                
menu = Menu()
menu.opciones()
