from Menu import menu

from PlanAhorro import plan
def test():
    unPlan = plan('12AB25X', 'Motomel', 'XLR-8', 450000)
    print('{}'.format(unPlan.mostrar()))
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