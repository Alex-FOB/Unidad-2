class registro:
    __temperatura = 0.0
    __humedad = 0.0
    __presion_atm = 0.0
    def __init__(self, temp = 0.0, humedad = 0.0, presion = 0.0):
        self.__temperatura = float(temp)
        self.__humedad = float(humedad)
        self.__presion_atm = float(presion)
    def __str__(self):
        return '{:5} {:12} {:12}'.format(self.__temperatura, self.__humedad, self.__presion_atm)
    def getTemp(self):
        return self.__temperatura
    def getHum(self):
        return self.__humedad
    def getPresion(self):
        return self.__presion_atm
    def getParametros(self):
        return [self.__temperatura, self.__humedad, self.__presion_atm]