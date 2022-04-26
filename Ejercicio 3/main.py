from Manejador import manejador
from Menu import menu
if __name__ == '__main__':
    print('INICIO ----Ejercicio 3----')
    band = False
    inter = menu()
    while not band:
        print('MENU:\n1.- Mostrar maximos y minimos\n2.- Promedio mensual de temperatura'
              '\n3.- Listar resgitro de dia\n4.- Salir')
        op = int(input('Opcion: '))
        inter.opcion(op)
        band = op == 4
    print('FINALIZANDO...')
    input()