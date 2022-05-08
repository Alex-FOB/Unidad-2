from Manejador import Control

class Interfaz:
    __op = None
    __funcion = None
    __manejador = None
    def __init__(self):
        self.__op = {1: self.punto1, 2: self.punto2, 3: self.punto3, 4: self.salir}
        self.__manejador = Control()
        self.__manejador.crearLista()
    def opcion(self, op):
        self.__funcion = self.__op.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
    def verificacion(self): #verifica el contenido de la lista
        if(self.__manejador.verificarLista() == True):
            print('La lista se creo correctamente')
        else:
            print('ERROR: la lista no se creó')
    def punto1(self): #compara las millas ingresadas con las de los viajeros
        millas = float(input('Ingrese millas: '))
        lista = self.__manejador.punto1(millas)
        if(len(lista) > 0):
            for viajero in lista:
                print(viajero)
        else:
            print('ERROR: no se encontro viajeros')
        input()
    def punto2(self): #acumula millas INVERTIDA
        nombre = str(input('Apellido y Nombre del viajero: '))
        pos = self.__manejador.buscar(nombre)
        if(pos != -1):
            print('Viajero: {}\nLA SUMA ES INVERTIDA'.format(self.__manejador.mostrar(pos)))
            millas = float(input('{} millas + '.format(self.__manejador.mostrarMillas(pos))))
            print('Resultado: {}'.format(self.__manejador.punto2(pos, millas)))
        else:
            print('ERROR: viajero no encontrado')
        input()
    def punto3(self): #canjea millas INVERTIDA
        nombre = str(input('Apellido y Nombre del viajero: '))
        pos = self.__manejador.buscar(nombre)
        if(pos != -1):
            print('Viajero: {}\nMillas - {}'.format(self.__manejador.mostrar(pos), self.__manejador.mostrarMillas(pos)))
            millas = float(input('Millas: '))
            resultado = self.__manejador.punto3(pos, millas) 
            if(resultado != -1): #compara el resultado y las muestra si no es negativo
                print('Resultado: {}'.format(resultado))
            else:
                print('ERROR: millas negativo')
        else:
            print('ERROR: viajero no encontrado')
        input()
    def salir(self):
        print('FINALIZANDO...')
        input()