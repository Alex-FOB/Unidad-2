import csv 

import numpy as np

from Cama import cama

class manejadorCamas:
    __lista = None #es un arreglo de elementos, no una lista
    __documento = None
    __dimension = 0
    __i = 0
    def __init__(self):
        self.__documento = open('Integrador\camas.csv')
        self.__lista = np.empty(self.__dimension, dtype = cama)
    def crearLista(self): # se crea la lista con las 30 camas
        band = False
        reader = csv.reader(self.__documento, delimiter = ';') #se lee el archivo
        self.__dimension = 30
        self.__lista.resize(self.__dimension) #se le da la dimensión al arreglo
        for fila in reader:
            if(band == False): #se saltea la primero fila del archivo
                band = True
            else:
                unaCama = cama(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.__lista[self.__i] = unaCama
                self.__i += 1
        #opcional:-------------------------
        while self.__i < len(self.__lista): #aquí se crean las otras camas sobrantes para completar las 30
            unaCama = cama(self.__i+1) #se le coloca el n° de cama
            self.__lista[self.__i] = unaCama
            self.__i += 1
        #----------------------------------
        self.__documento.close()
    def verificacion(self): #se verifica el contenido del arreglo
        band = 'VACIO'
        if(len(self.__lista) > 0):
            band = 'LISTO'
        return band
    def buscarPaciente(self, paciente): #se busca el paciente y retorna la posición en el arreglo
        retorno = [-1, None]
        i = 0
        band = False
        while not band and i < len(self.__lista):
            if(self.__lista[i].getPaciente() == paciente): #se compara el paciente con lo que se ingresó
                retorno[0] = i
                retorno[1] = self.__lista[i].getIdCama()
                band = True 
            i += 1
        return retorno
    def mostrar(self): #muestra todo el contenido del arreglo
        text = ''
        for cama in self.__lista:
            text += '{}'.format(cama) + '\n'
        return text #se retorna un texto con el contenido del arreglo
    def mostrarPaciente(self, id): #muestra un paciente determinado
        cadena = '{}'.format(self.__lista[id])
        return cadena
    def mostrarDiag(self, diagnostico): #muestra los pacientes con el diagnostico ingrasado
        text = ''
        for cama in self.__lista:
            if(cama.getPaciente() != None and cama.getDiag() == diagnostico):
                text += '{}'.format(cama) + '\n'
        return text #se retorna un texto que contiene a los pacientes y sus datos