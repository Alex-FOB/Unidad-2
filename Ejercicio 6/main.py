from Menu import Interfaz

from ViajeroFrecuente import viajero

def test():
    unViajero = viajero(1, '42805869', 'Gonzalo', 'Peralta', 5000)
    print(unViajero)
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        menu = Interfaz()
        menu.verificacion()
        band = False
        while not band:
            print('----Ejercicio 6----\n1.- Mayor cantidad de millas acumuladas\n2.- Acumular millas\n3.- Canjear millas\n'
                '4.- Salir')
            op = int(input('Opcion: '))
            menu.opcion(op)
            band = op == 4