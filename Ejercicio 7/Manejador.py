import csv

from ViajeroFrecuente import viajero

class Control:
    __lista = []
    __documento = None
    def __init__(self):
        self.__lista = []
        self.__documento = open('Actividad 7\Viajeros.csv')
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
    def verificarLista(self): #verifica el contenido de la lista
        band = False
        if(len(self.__lista) > 0): #verifica la longitud de la lista
            band = True
        return band
    def buscar(self, nomCompleto = 'unknown'): #en base a un viajero ingresado devuelve su posición en la lista
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
    def punto1(self, num): #compara las millas ingresadas con las de los viajeros
        lista = []
        for viajero in self.__lista:
            if(num == viajero.getMillas()): #Ej: 100 == Viajero
                lista.append(viajero)
        return lista
    def punto2(self, pos, millas): #acumula millas INVERTIDA
        return millas + self.__lista[pos] #Ej: 100 + Viajero
    def punto3(self, pos, millas): #canjea millas INVERTIDA
        resultado = -1
        if(millas >= self.__lista[pos].getMillas()): #compara que las millas ingresadas no sean mayor o igual a las del viajero
            resultado = millas - self.__lista[pos] #Ej: 100 - Viajero
        return resultado
    def mostrar(self, pos): #muestra los datos del viajero
        return self.__lista[pos].getViajero()
    def mostrarMillas(self, pos): #muestra las millas del viajero
        return self.__lista[pos].getMillas()