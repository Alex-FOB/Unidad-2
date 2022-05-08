from Controlador import control

class menu:
    __op1 = None
    __op2 = None
    __funcion = None
    __controlador = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.punto4, 5: self.salir}
        self.__controlador = control()
        self.__controlador.crearLista()
    def opción(self, op):
        self.__funcion = self.__op.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def buscar(self): #permite buscar un plan de la lista
        print('Ingrese plan a buscar')
        codigo = str(input('Codigo de plan: '))
        return self.__controlador.getPlan(codigo)
    def mostrar(self): #muestra el contenido de la lista
        planes = self.__controlador.mostrar()
        print(planes)
    def punto1(self):
        self.mostrar()
        pos = self.buscar()
        if(pos != False):
            monto = float(input('Monto nuevo: $'))
            self.__controlador.punto1(monto, pos)
            print(self.__controlador)
        else:
            print('ERROR: codigo de vehiculo invalido')
        input()
    def punto2(self):
        valor = float(input('Ingrese valor de cuota: $'))
        print('Vehículos con valor de cuota menor a ${:2}\n{}'.format(valor, self.__controlador.punto2(valor)))
        input()
    def punto3(self): #PREGUNTAR
        cuotas = input('Modificar cuotas del vehiculo: ')
        print(self.__controlador.punto3(cuotas))
        input()
    def punto4(self):
        cuotas = input('Modificar cuotas pagadas para solicitar: ')
        print(self.__controlador.punto4(cuotas))
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()