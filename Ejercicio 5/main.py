from Menu import menu

from Controlador import control
def test():
    manejador = control()
    manejador.crearLista()
    print('Ingresar datos:')
    cod = int(input('Código de plan: '))
    modelo = str(input('Modelo del vehiculo: '))
    version = str(input('Version del vehiculo: '))
    valor = float(input('Valor del vehiculo: '))
    cuotas = int(input('Cuotas del plan: '))
    pagas = int(input('Cuotas pagadas para solicitar: '))
    print(manejador.test(cod, modelo, version, valor, cuotas, pagas))
    input()
if __name__ == '__main__':
    if(str(input('¿Testear? ')).lower() == 'si'):
        test()
    else:
        interfaz = menu()
        band = False
        while not band:
            print('----EJERCICO 5----\n1.- Actualizar valor del vehículo\n2.- Mostrar monto para solicitar'
                  '\n3.- Modificar cuotas para solicitar\n4.- Modificar cuotas pagadas para solicitar\n5.- Salir')
            op = int(input('Opcion: '))
            interfaz.opción(op)
            band = op == 5
        print('FINALIZANDO...')
        input()