from Menu import Interfaz

def test():
    pass
if __name__ == '__main__':
    menu = Interfaz()
    menu.verificacion()
    band = False
    while not band:
        print('----Ejercicio 6----\n1.- Comparar millas\n2.- Acumular millas\n3.- Canjear millas\n'
              '4.- Salir')
        op = int(input('Opcion: '))
        menu.opcion(op)
        band = op == 4