from Menu import menu

from ViajeroFrecuente import viajero

def test():
    unViajero = viajero(1, '42805869', 'Gonzalo', 'Peralta', 5000)
    print(unViajero)
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        band = False
        interfaz = menu()
        while not band:
            print('Ejercicio 2:\n1.- Buscar viajero\n2.- Salir')
            op = int(input('Opcion: '))
            interfaz.opción1(op)
            band = op == 2