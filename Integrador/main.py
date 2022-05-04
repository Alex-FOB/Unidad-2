from Menu import interfaz

from Cama import cama

from Medicamentos import medicamento

def test(): #se comprueba la creacion de las instancias de la clase cama y medicamento
    unaCama = cama(28, 100, True, 'Aguero, Alex', 'Cancer de todo', '28/07/20222')
    print(unaCama)
    unMedicamento = medicamento(1, 20, 'Levitra', 'Vardenafil', 'Pastilla', '50mg', 1700)
    print(unMedicamento)
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        band = False
        menu = interfaz()
        while not band:
            bandera = menu.verificacion()
            print('1.- Crear lista cama: {}\n2.- Crear lista medicamentos: {}\n3.- Buscar paciente\n4.- Listar pacientes\n5.- Salir'.format(bandera[0], bandera[1]))
            op = int(input('Opcion: '))
            menu.opcion(op)
            band = op == 5