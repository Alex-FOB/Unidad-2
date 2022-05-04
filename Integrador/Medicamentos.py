class medicamento:
    __idCama = 0
    __idMedicamento = 0
    __nombre = '' #nombre comercial
    __monodroga = ''
    __presentacion = ''
    __cantApli = ''
    __precio = 0.0
    def __init__(self, idCama = 0, idMed = 0, nom = '?', mono = '?', pres = '?', cant = '?', precio = 0.0):
        if(int(idCama) <= 30 and int(idCama) >= 1 and int(idMed) <= 100 and int(idMed) >= 1):
            self.__idCama = int(idCama)
            self.__idMedicamento = int(idMed)
            self.__nombre = str(nom)
            self.__monodroga = str(mono)
            self.__presentacion = str(pres)
            self.__cantApli = str(cant)
            self.__precio = float(precio)
    def __str__(self): #premite mostrar ciertos datos de una instancia medicamento
        return '{}/{:20} {:20} {:11}   ${:>}'.format(self.__nombre, self.__monodroga, self.__presentacion, self.__cantApli, self.__precio)
    def getIdCama(self): #da la id de la cama
        return self.__idCama
    def getPrecio(self): #da el precio del medicamento
        return self.__precio