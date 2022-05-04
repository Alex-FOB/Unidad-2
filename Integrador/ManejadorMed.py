from cgitb import text
import csv

from Medicamentos import medicamento

class manejadorMed: #manejador de medicamentos
    __lista = []
    __documento = None
    def __init__(self):
        self.__documento = open('Integrador\medicamentos.csv')
    def crearLista(self): #se crea la lista con los medicamentos
        band = False
        reader = csv.reader(self.__documento, delimiter = ';') #se lee el archivo
        for fila in reader:
            if(band == False): #se saltea la primera fila del archivo
                band = True
            else:
                unMed = medicamento(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])
                self.__lista.append(unMed)
        self.__documento.close()
    def verificacion(self): #se verifica el contenido de la lista
        band = 'VACIO'
        if(len(self.__lista) > 0):
            band = 'LISTO'
        return band
    def totalPaciente(self, id): #calcula el importe total que un paciente debe pagar por los medicamentos
        acum = 0.0
        for med in self.__lista:
            if(med.getIdCama() == id):
                acum += med.getPrecio()
        return acum
    def medPaciente(self, id): #retorna los medicamentos que se le dio a un paciente
        text = ''
        for med in self.__lista:
            if(med.getIdCama() == id):
                text += '{}'.format(med) + '\n'
        return text
    def mostrar(self): #muestra el contenido de la lista
        text = ''
        for med in self.__lista:
            text += '{}'.format(med) + '\n'
        return text