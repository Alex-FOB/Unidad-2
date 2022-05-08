import csv

from PlanAhorro import plan

class control:
    __lista = []
    __documento = None
    def __init__(self):
        self.__lista = []
        self.__documento = open('Actividad 5\planes.csv')
    def crearLista(self): #crea la lista
        reader = csv.reader(self.__documento, delimiter = ";")
        band = False
        for fila in reader:
            unPlan = plan(fila[0], fila[1], fila[2], fila[3])
            if(band == False):
                plan.actCuotas(fila[4])
                plan.actCuotasPagas(fila[5])
                band = True
            self.__lista.append(unPlan)
        self.__documento.close()
    def mostrar(self): #muestra el contenido de la lista
        texto = ''
        for plan in self.__lista:
            texto += plan.mostrar() + '\n'
        return texto
    def getPlan(self, codigo): #devuelve la posción de un plan en base al código ingresado
        band = False
        i = 0
        pos = 0
        while not band:
            if(i == len(self.__lista)):
                band = True
                pos = False
            elif(self.__lista[i].getCodigo() == codigo):
                pos = i
                band = True
            i += 1
        return pos
    def punto1(self, monto, pos): #actualiza el valor del plan
        self.__lista[pos].actValor(monto)
    def punto2(self, valor): #en base a un importe de cuota, busca los planes 
        texto = ''
        for plan in self.__lista:
            cuotas = plan.getCuotas()
            if(plan.calcImporteCouta(cuotas) < valor):
                texto += plan.mostrar() + '\n'
        if(len(texto) == 0):
            texto = 'NO HAY'
        return texto
    def punto3(self, cuotas): #actualiza las cuotas de los planes
        plan.actCuotas(cuotas) #variable de clase
        return plan.mostrarVariablesClase()
    def punto4(self, cuotas): #actualiza las cuotas que se deben tener pagadas para solicitar el vehículo
        plan.actCuotasPagas(cuotas) #variable de clase
        return plan.mostrarVariablesClase()