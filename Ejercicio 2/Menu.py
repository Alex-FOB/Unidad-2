from Manejador import manejador

class menu:
    __op1 = None
    __op2 = None
    __funcion = None
    __control = None
    def __init__(self):
        self.__op1 = {1: self.punto1, 2: self.cerrar}
        self.__op2 = {1: self.consultar, 2: self.acumular, 3: self.canjear, 4: self.salir}
        self.__control = manejador()
        self.__control.crearListaViajeros()  # se crea la lista de viajeros
    def opción1(self, op):  #primer menú
        self.__funcion = self.__op1.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def opción2(self, op, i): #segundo menú
        self.__funcion = self.__op2.get(op)
        if self.__funcion:
            self.__funcion(i)
        else:
            print('ERROR: opcion invalida')
        input()
    def punto1(self):
        num = int(input('Ingrese el numero de viajero: '))
        i = self.__control.buscar(num)
        band = False
        if (i != -1):
            while not band: #hacer que dure el segundo menú
                print(
                    '{}\nOPCIONES DE VIAJERO:\n1.- Consultar cantidad de millas\n2.- Acumular millas\n'
                    '3.- Canjear millas\n4.- Salir'.format(self.__control.buscarNom(i)))
                op = int(input('Opcion: '))
                self.opción2(op, i)
                band = op == 4
        else:
            print('ERROR: numero de viajero invalido')
            input()
    def consultar(self, i):
        print('Millas acumuladas: {}'.format(self.__control.consultar(i)))
    def acumular(self, i):
        millas = int(input('Millas acumular: '))
        print('Millas totales: {}'.format(self.__control.acumular(i, millas)))
    def canjear(self, i):
        canjear = int(input('Millas a canjear: '))
        if(self.__control.canjear(i, canjear) == True):
            print('Se han canjeado {} millas'.format(canjear))
        else:
            print('ERROR: no se pudo canjear')
    def salir(self, i = 0):
        pass
    def cerrar(self):
        self.__control.cerrarArchivo()