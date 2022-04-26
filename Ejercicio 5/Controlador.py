import csv

from PlanAhorro import plan

class control:
    __lista = []
    __documento = None
    def __init__(self):
        self.__lista = []
        self.__documento = open('planes.csv')
    def crearLista(self):
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
    def mostrar(self):
        texto = ''
        for plan in self.__lista:
            texto += plan.mostrar() + '\n'
        return texto
    def getPlan(self, codigo): #Devuelve la posción de un plan en base al código ingresado
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
    def punto1(self, monto, pos):
        self.__lista[pos].actValor(monto)
    def punto2(self, valor):
        texto = ''
        for plan in self.__lista:
            cuotas = plan.getCuotas()
            if(plan.calcImporteCouta(cuotas) < valor):
                texto += plan.mostrar() + '\n'
        if(len(texto) == 0):
            texto = 'NO HAY'
        return texto
    def punto3(self, cuotas):
        plan.actCuotas(cuotas)
        return plan.mostrarVariablesClase()
    def punto4(self, cuotas):
        plan.actCuotasPagas(cuotas)
        return plan.mostrarVariablesClase()
    #Verificar si se crean planes de ahorro
    def test(self, cod, modelo, version, valor, cuotas, pagas):
        unPlan = plan(cod, modelo, version, valor, cuotas, pagas)
        return unPlan