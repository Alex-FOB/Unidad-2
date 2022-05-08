class plan:
    #variables de clase
    cuotas = 0 #cantidad de cuotas totales
    cuotasPagas = 0 #cantidad de coutas que debe tener pagadas para solicitar el vehículo
    def __init__(self, codigo = 'unknown', modelo = 'unknown', version = 'unknown', valor = 0.0):
        self.__código = str(codigo)
        self.__modelo = str(modelo)
        self.__version = str(version)
        self.__valor = float(valor)
    #Métodos de instancia
    def mostrar(self):
        return 'Codigo: {} - Modelo/version: {}/{}'.format(self.__código, self.__modelo,self.__version)
    def getCodigo(self):
        return self.__código
    def calcImporteCouta(self, cantCuotas):
        return (self.__valor / cantCuotas) + self.__valor * 0.1
    def actValor(self, valor):
        self.__valor = valor
    def montoLicita(self, imp):
        return self.__coutasPagas * self.calcImporteCouta()
    def modCuotasPagas(self, cantidad):
        pass
    #Métodos de clase
    @classmethod
    def getCuotas(cls):
        return cls.cuotas
    @classmethod
    def actCuotas(cls, cantidad):
        cls.cuotas = int(cantidad)
    @classmethod
    def actCuotasPagas(cls, cantidad):
        cls.cuotasPagas = int(cantidad)
    @classmethod
    def mostrarVariablesClase(cls):
        return 'Cuotas: {} - Cuotas pagadas para solicitar: {}'.format(cls.cuotas, cls.cuotasPagas)