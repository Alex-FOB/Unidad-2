from ViajeroFrecuente import viajero

import csv

class manejador:
    __documento = None
    __lista = []
    def __init__(self): #abre el archivo csv
        self.__documento = open('Viajeros.csv')
    def crearListaViajeros(self):
        reader = csv.reader(self.__documento, delimiter = ';')
        band = True
        for fila in reader:
            if(band == True):
                band = False
            else:
                unViajero = viajero(fila[0], str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
                self.__lista.append(unViajero)
    def buscar(self, num):
        i = -1
        band = False
        pos = 0
        while (i < len(self.__lista) and band == False):
            i += 1
            if (num == self.__lista[i].getNum()):
                pos = i
                band = True
        return pos
    def buscarNom(self, i):
        return self.__lista[i].getNom()
    def consultar(self, i):
        return self.__lista[i].cantidadTotaldeMillas()
    def acumular(self, i, millas):
        return self.__lista[i].acumularMillas(millas)
    def canjear(self, i, canjear):
        band = False
        if(canjear <= self.__lista[i].cantidadTotaldeMillas()):
            self.__lista[i].canjearMillas(canjear)
            band = True
        return band
    def cerrarArchivo(self):
        self.__documento.close()