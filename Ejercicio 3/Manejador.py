import csv

from Registro import registro

class manejador:
    __lista = []
    __documento = None
    def __init__(self):
        self.__lista = []
    def lecturaLista(self): #se lee el archivo para obtener la cantidad de días que contiene
        self.__documento = open('Actividad 3\RegistroMeteorologico.csv')
        reader = csv.reader(self.__documento, delimiter = ';')#luego cambiar a ;
        band = True
        dias = 0
        for fila in reader:
            if(band == True):
                band = False
            else:
                if(fila[1] == '23'):
                    dias += 1
        self.__documento.close()
        return dias #devuelve la cantidad de días
    def crearLista(self, dias): #se crea la lista
        horas = 24
        d = 0
        self.__lista = [[]for i in range(dias)] #se define la lista bidimensional
        self.__documento = open('Actividad 3\RegistroMeteorologico.csv')
        reader = csv.reader(self.__documento, delimiter=';')#cambiar a ;
        band = True
        for fila in reader:
            if(band == True):
                band = False
            else:
                if(horas != 0):
                    unRegistro = registro(fila[2], fila[3], fila[4])
                    self.__lista[d].append(unRegistro)
                    horas -= 1
                else:
                    d += 1
                    horas = 24
                    unRegistro = registro(fila[2], fila[3], fila[4])
                    self.__lista[d].append(unRegistro)
        self.__documento.close()
    #punto 1
    def punto1Max(self, pos): #busca el (temperatura, humedad, presión) máxima
        d = 1
        h = 0
        dMax = 0
        hMax = 0
        max = -20
        for dia in self.__lista:
            for hora in dia:
                lista = hora.getParametros()
                if(lista[pos] > max):
                    max = lista[pos]
                    dMax = d
                    hMax = h
                h += 1
            h = 0
            d += 1
        return [dMax, hMax, max]
    def punto1Min(self, pos): #busca el (temperatura, humedad, presión) mínima
        d = 1
        h = 0
        dMin = 0
        hMin = 0
        min = 15000
        for dia in self.__lista:
            for hora in dia:
                lista = hora.getParametros()
                if (lista[pos] < min):
                    min = lista[pos]
                    dMin = d
                    hMin = h
                h += 1
            h = 0
            d += 1
        return [dMin, hMin, min]
    #punto 2
    def punto2(self): #calcular promedio de temperatura de un mes por hora
        cont = [0.0]*24
        acum = [0.0]*24
        lista = []
        indice = 0
        for dia in self.__lista:
            for hora in dia:
                acum[indice] += float(hora.getTemp())
                cont[indice] += 1
                indice += 1
            indice = 0
        for i in range(24):
            lista.append(acum[i]/cont[i])
        return lista
    #punto 3
    def punto3(self, dia): #listar temperatura de un día
        return self.__lista[dia]