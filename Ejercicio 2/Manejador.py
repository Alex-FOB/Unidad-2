import csv

from ViajeroFrecuente import viajero

class manejador:
    __documento = None
    __lista = []
    def __init__(self): #abre el archivo csv
        self.__documento = open('Actividad 2\Viajeros.csv')
    def crearListaViajeros(self): #se crea la lista con los datos del archivo
        reader = csv.reader(self.__documento, delimiter = ';') #lee el archivo
        band = True
        for fila in reader:
            if(band == True):
                band = False
            else:
                unViajero = viajero(fila[0], str(fila[1]), str(fila[2]), str(fila[3]), float(fila[4]))
                self.__lista.append(unViajero)
    def buscar(self, num): #busca el viajero ingresado en la lista y devuelve su posición en la lista
        i = -1
        band = False
        pos = 0
        while (i < len(self.__lista) and band == False):
            i += 1
            if (num == self.__lista[i].getNum()):
                pos = i
                band = True
        return pos
    def buscarNom(self, i): #devuelve el nombre del viajero
        return self.__lista[i].getNom()
    def consultar(self, i): #devuelve la cantidad total de millas acumuladas del viajero
        return self.__lista[i].cantidadTotaldeMillas()
    def acumular(self, i, millas): #devuelve el resultado de sumar las millas ingresadas con las del viajero
        return self.__lista[i].acumularMillas(millas)
    def canjear(self, i, canjear): #devuelve el resultado de restar las millas ingresadas con las del viajero
        band = False
        if(canjear <= self.__lista[i].cantidadTotaldeMillas()): #verifica que las millas ingresadas no sean mayores a las del viajero
            self.__lista[i].canjearMillas(canjear)
            band = True
        return band
    def cerrarArchivo(self): #cierra el archivo
        self.__documento.close()