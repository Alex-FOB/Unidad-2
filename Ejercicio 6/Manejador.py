import csv

from ViajeroFrecuente import viajero

class Control:
    __lista = []
    __documento = None
    def __init__(self):
        self.__lista = []
        self.__documento = open('Viajeros.csv')
    def crearLista(self):
        reader = csv.reader(self.__documento, delimiter = ';')
        band = False
        for fila in reader:
            if(band == False):
                band = True
            else:
                unViajero = viajero(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__lista.append(unViajero)
        self.__documento.close()
    def verificarLista(self):
        band = False
        if(len(self.__lista) > 0):
            band = True
        return band
    def buscar(self, nomCompleto = 'unknown'):
        band = False
        i = 0
        pos = 0
        while not band:
            if (i == len(self.__lista)):
                band = True
                pos = -1
            else:
                if(self.__lista[i].getViajero() == nomCompleto):
                    pos = i
                    band = True
            i += 1
        return pos
    def punto1(self):
        max = viajero(0, 'unknown', 'unknown', 'unknown', 0)
        pos = 0
        for i in range(len(self.__lista)):
            if(self.__lista[i] > max): #Ej: Viajero > maximo
                max = self.__lista[i]
                pos = i
        return pos
    def punto1Verf(self, pos): #Sirve para verificar cuantos viajeros tienen la misma cantidad de millas máximas
        viajeros = []
        for viajero in self.__lista:
            if(viajero == self.__lista[pos]):
                viajeros.append(viajero)
        return viajeros
    def punto2(self, pos, millas):
        return self.__lista[pos] + millas #Ej: Viajero + 100
    def punto3(self, pos, millas):
        resultado = -1
        if(millas <= self.__lista[pos].getMillas()):
            resultado = self.__lista[pos] - millas #Ej: Viajero - 100
        return resultado
    def mostrar(self, pos):
        return self.__lista[pos].getViajero()
    def mostrarMillas(self, pos):
        return self.__lista[pos].getMillas()
    #testeo de creacion de instancias Viajero
    def test(self):
        pass