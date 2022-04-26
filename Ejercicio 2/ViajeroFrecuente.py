class viajero:
    __num_viajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = 0
    def __init__(self, num = 0, dni = 'unknown', nom = 'unknown', ape = 'unknown', millas = 0.0):
        self.__num_viajero = int(num)
        self.__dni = str(dni)
        self.__nombre = str(nom)
        self.__apellido = str(ape)
        self.__millas = float(millas)
    def cantidadTotaldeMillas(self):
        return self.__millas
    def acumularMillas(self, millas):
        self.__millas += millas
        return self.__millas
    def canjearMillas(self, canjeo):
        self.__millas -= canjeo
        return self.__millas
    #MÉTODOS AGREGADOS
    def getNum(self):
        return self.__num_viajero
    def getNom(self):
        return '{} {}'.format(self.__nombre, self.__apellido)