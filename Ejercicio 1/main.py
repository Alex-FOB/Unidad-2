from Manejador import control

from Email import correo

def test(): #se prueba la creación de instacia de la clase email
    unCorreo = correo('pepe', 'hotmail', 'com')
    print('{}'.format(unCorreo.retornaEmail()))
def main(): #se muestran las opciones
    manejador = control()
    salir = False
    while not salir:
        print('Ejercicio 1:\nDATO: la contraseña default es "unknown"\nLista del documento: {}'
              '\n1.- Crear cuenta\n2.- Modificar contraseña\n3.- Crear objeto\n4.- Leer archivo'
              '\nADICIONALES\n5.- Mostrar\n6.- Salir'.format(manejador.verDocumento()))
        op = int(input('Opcion: '))
        if(op == 1):  # punto 1
            punto1(manejador)
        if(op == 2):  # punto 2
            punto2(manejador)
        if(op == 3):  # punto 3
            punto3(manejador)
        if(op == 4):  # punto 4
            punto4(manejador)
        if(op == 5):
            punto5(manejador)
        salir = op == 6
def punto1(manejador): #se crea un correo ingrasando id, dominio y tipo de dominio
    print('----CREAR CUENTA----')
    nombre = str(input('Ingrese su nombre: '))
    # nomCuenta = str(input('Igrese su nombre de cuenta de correo: '))
    id = str(input('Ingrese el identificador de cuenta: '))
    dominio = str(input('Ingrese el dominio de cuentra: '))
    tipo = str(input('Igrese el tipo de dominio de cuenta: '))
    if(manejador.verificar('{}@{}.{}'.format(id, dominio, tipo)) == False):
        manejador.punto1(id, dominio, tipo)  # se crea el correo
        print('Estimado {} te enviaremos tus mensajes a la dirección {}@{}.{}'
              .format(nombre, id, dominio, tipo))
    else:
        print('ERROR: correo ya registrado')
    input()
def punto2(manejador): #se cambia la contraseña del correo creado
    print('----MODIFICAR CONTRASEÑA----\n1.- Modificar contraseña de la instancia\n2.- Modificar contraseña'
          ' del documento')
    eleccion = int(input('Opcion: '))
    if(eleccion == 1): #opción modificar la contraseña de los correos de la lista creada a mano
        correo = str(input('Ingrese correo: '))
        if(manejador.verificar(correo) == True): #verifica que el correo ingrasado esté en la lista
            contraseña = str(input('Ingrese contraseña actual: '))
            if(manejador.verificarContra1(correo, contraseña) == True): #se verifica que la contraseña ingresada sea la misma a la anterior
                contraseña = str(input('Ingrese contraseña nueva: '))
                manejador.punto2uno(correo, contraseña)
                print('Contraseña se modifico correctamente')
            else:
                print('ERROR: la contraseña no es la misma')
        else:
            print('ERROR: correo no registrado')
    else: #opción modificar la contraseña de los correos de la lista creada con el documento
        correo = str(input('Ingrese correo: '))
        if(manejador.buscar(correo) >= 1): #verifica que el correo ingresado esté en la lista
            contraseña = str(input('Ingrese contraseña actual: '))
            if(manejador.verificarContra2(correo, contraseña) == True): #se verifica que la contraseña ingresada sea la misma a la anterior
                contraseña = str(input('Ingrese contraseña nueva: '))
                manejador.punto2dos(correo, contraseña)
                print('Contraseña se modifico correctamente')
            else:
                print('ERROR: la contraseña no es la misma')
        else:
            print('ERROR: correo no registrado')
    input()
def punto3(manejador): #se crea un correo con "ejemplo@ejemplo.ejemplo"
    print('----CREAR CUENTA 2----\nEj: unkown@unkown.unkown')
    correo = str(input('Ingrese correo: '))
    if(manejador.verificar(correo) == False): #verifica que el correo ingresado no haya sido creado
        manejador.punto3(correo)
        print('Su correo ha sido creado')
    else:
        print('ERROR: correo ya registrado')
    input()
def punto4(manejador): #crea la lista con los correos del documento y se verifica si hay repetidos
    if(manejador.verificarLista()): #verifica el contenido de la lista de los correos del documento
        manejador.punto4()
        print('Se han creado los correos correctamente')
        correo = str(input('Correo a buscar: '))
        if(manejador.buscar(correo) > 1):
            print('El correo {} se encuentra repetido'.format(correo))
        else:
            print('El correo {} no se encuentra repetido'.format(correo))
    else: #cuando ya está creada
        correo = str(input('Correo a buscar: '))
        if(manejador.buscar(correo) > 1):
            print('El correo {} se encuentra repetido'.format(correo))
        else:
            print('El correo {} no se encuentra repetido'.format(correo))
    input()
def punto5(manejador): #muestra el contenido de ambas listas
    manejador.mostrar()
    input()
if __name__ == '__main__':
    if(str(input('¿Desea testear? ')).lower() == 'si'):
        test()
    else:
        main()
        print('FINALIZANDO...')
        input()