from Manejador import control

def tester():
    pass
def main():
    manejador = control()
    salir = False
    while not salir:
        print('Ejercicio 1:\nDATO: la contraseña default es "unknown"\nLista del documento: {}'
              '\n1.- Crear cuenta\n2.- Modificar contraseña\n3.- Crear objeto\n4.- Leer archivo'
              '\nADICIONALES\n5.- Buscar correo repetido(4)\n6.- Mostrar\n7.- Salir'.format(manejador.verDocumento()))
        op = int(input('Opcion: '))
        if (op == 1):  # punto 1
            punto1(manejador)
        if (op == 2):  # punto 2
            punto2(manejador)
        if (op == 3):  # punto 3
            punto3(manejador)
        if (op == 4):  # punto 4
            punto4(manejador)
        if (op == 5):
            punto5(manejador)
        if (op == 6):
            punto6(manejador)
        salir = op == 7
def punto1(manejador):
    print('----CREAR CUENTA----')
    nombre = str(input('Ingrese su nombre: '))
    # nomCuenta = str(input('Igrese su nombre de cuenta de correo: '))
    id = str(input('Ingrese el identificador de cuenta: '))
    dominio = str(input('Ingrese el dominio de cuentra: '))
    tipo = str(input('Igrese el tipo de dominio de cuenta: '))
    if (manejador.verificar('{}@{}.{}'.format(id, dominio, tipo)) == False):
        manejador.punto1(id, dominio, tipo)  # se crea el correo
        print('Estimado {} te enviaremos tus mensajes a la dirección {}@{}.{}'
              .format(nombre, id, dominio, tipo))
    else:
        print('ERROR: correo ya registrado')
    input()
def punto2(manejador):
    print('----MODIFICAR CONTRASEÑA----\n1.- Modificar contraseña de la instancia\n2.- Modificar contraseña'
          ' del documento')
    eleccion = int(input('Opcion: '))
    if (eleccion == 1):
        correo = str(input('Ingrese correo: '))
        if (manejador.verificar(correo) == True):
            contraseña = str(input('Ingrese contraseña actual: '))
            if (manejador.verificarContra1(correo, contraseña) == True):
                contraseña = str(input('Ingrese contraseña nueva: '))
                manejador.punto2uno(correo, contraseña)
                print('Contraseña se modifico correctamente')
            else:
                print('ERROR: la contraseña no es la misma')
        else:
            print('ERROR: correo no registrado')
    else:
        correo = str(input('Ingrese correo: '))
        if (manejador.buscar(correo) >= 1):
            contraseña = str(input('Ingrese contraseña actual: '))
            if (manejador.verificarContra2(correo, contraseña) == True):
                contraseña = str(input('Ingrese contraseña nueva: '))
                manejador.punto2dos(correo, contraseña)
                print('Contraseña se modifico correctamente')
            else:
                print('ERROR: la contraseña no es la misma')
        else:
            print('ERROR: correo no registrado')
    input()
def punto3(manejador):
    print('----CREAR CUENTA 2----\nEj: unkown@unkown.unkown')
    correo = str(input('Ingrese correo: '))
    if (manejador.verificar(correo) == False):
        manejador.punto3(correo)
        print('Su correo ha sido creado')
    else:
        print('ERROR: correo ya registrado')
    input()
def punto4(manejador):
    manejador.punto4()
    print('Se han creado los correos correctamente')
    correo = str(input('Correo a buscar: '))
    if (manejador.buscar(correo) > 1):
        print('El correo {} se encuentra repetido'.format(correo))
    else:
        print('El correo {} no se encuentra repetido'.format(correo))
    input()
def punto5(manejador):
    if (manejador.punto5() == True):
        correo = str(input('Correo a buscar: '))
        if (manejador.buscar(correo) > 1):
            print('El correo {} se encuentra repetido'.format(correo))
        else:
            print('El correo {} no se encuentra repetido'.format(correo))
    else:
        print('ERROR: no se creo la lista de correos del documento')
    input()
def punto6(manejador):
    manejador.mostrar()
    input()
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        tester()
    else:
        main()
        print('FINALIZANDO...')
        input()