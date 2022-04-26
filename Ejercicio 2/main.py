from Menu import menu

if __name__ == '__main__':
    band = False
    interfaz = menu()
    while not band:
        print('Ejercicio 2:\n1.- Buscar viajero\n2.- Salir')
        op = int(input('Opcion: '))
        interfaz.opción1(op)
        band = op == 2
    print('FINALIZANDO...')
    input()