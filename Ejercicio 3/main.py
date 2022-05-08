from Menu import menu

from Registro import registro

def test():
    unReg = registro(38.9, 15, 1000.1)
    print(unReg)
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        print('INICIO ----Ejercicio 3----')
        band = False
        inter = menu()
        while not band:
            print('MENU:\n1.- Mostrar maximos y minimos\n2.- Promedio mensual de temperatura'
                '\n3.- Listar resgitro de dia\n4.- Salir')
            op = int(input('Opcion: '))
            inter.opcion(op)
            band = op == 4