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
    #Métodos de instancia
    def getMillas(self):
        return self.__millas
    def getViajero(self):
        return '{} {}'.format(self.__apellido, self.__nombre)
        #Sobrecarga de operadores
    def __str__(self):
        return '{} {}\nNumero: {} - DNI: {} - Millas: {}'.format(self.__apellido, self.__nombre, self.__num_viajero,
                                                                 self.__dni, self.__millas)
    def __gt__(self, other):
        return self.__millas > other.getMillas()
    def __add__(self, other):
        return self.__millas + other
    def __sub__(self, other):
        return self.__millas - other
    def __eq__(self, other):
        return self.__millas == other.getMillas()