from ManejadorCamas import manejadorCamas

from ManejadorMed import manejadorMed

class interfaz:
    __op = None
    __funcion = None
    __manejadorCama = None
    __manejadorMed = None
    __band = [None, None]
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.salir}
        self.__manejadorCama = manejadorCamas()
        self.__manejadorMed = manejadorMed()
    def opcion(self, op): #Con la función obtenida invoca la función
        self.__funcion = self.__op.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
    def punto1(self): #Crea la lista de las camas y las muestra
        if(self.__band[0] == 'VACIO'):
            self.__manejadorCama.crearLista()
            print(self.__manejadorCama.mostrar())
        else:
            print('ERROR: el arreglo ya esta creado')
        input()
    def punto2(self): #Crea la lista de los medicamentos y las muestra
        if(self.__band[1] == 'VACIO'):
            self.__manejadorMed.crearLista()
            print(self.__manejadorMed.mostrar())
        else:
            print('ERROR: la lista ya esta creada')
        input()
    def punto3(self): #Buscar paciente
        if(self.__band[0] == 'LISTO' and self.__band[1] == 'LISTO'): #comprueba que las listas esten creadas
            paciente = str(input('Ingrese "Apellido, Nombre" del paciente: '))
            pos = self.__manejadorCama.buscarPaciente(paciente)
            if(pos[0] != -1): #comprueba que el paciente este en la lista
                print('{}'.format(self.__manejadorCama.mostrarPaciente(pos[0])))
                print('Medicamento/monodroga        Presentacion        Cantidad        Precio')
                print('{}'.format(self.__manejadorMed.medPaciente(pos[1])))
                total = self.__manejadorMed.totalPaciente(pos[1])
                print('Total adeudado:                                                  ${}'.format(total))
            else:
                print('ERROR: paciente no identificado')
        else:
            print('ERROR: alguna de las dos listas no está cargada')
        input()
    def punto4(self): #Buscar pacientes
        if(self.__band[0] == 'LISTO'): #compureba que las lista cama este creada
            diag = str(input('Ingrese diagnostico: '))
            text = self.__manejadorCama.mostrarDiag(diag)
            if(len(text) != 0): #comprueba que se haya encontrado un paciente
                print(text)
            else:
                print('ERROR: diagnostico no encontrado')
        else:
            print('ERROR: alguna de las dos listas no está cargada')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()
    #Adicional
    def verificacion(self): #Verifica el contenido de las listas de Camas y Medicamentos
        self.__band[0] = self.__manejadorCama.verificacion()
        self.__band[1] = self.__manejadorMed.verificacion()
        return self.__band