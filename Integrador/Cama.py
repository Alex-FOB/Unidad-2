class cama:
    __idCama = 0
    __habitacion = 0
    __estado = False
    __paciente = None
    __diagnostico = 'unknown'
    __fechaInternacion = None
    __fechaAlta = None
    def __init__(self, id = 0, hab = 0, estado = False, paciente = '', diag = '', fInter = '', fAlta = None):
        if(int(id) <= 30 and int(id) >= 1): #verifica que esté en el rango de la cantidad de camas disponibles
            self.__idCama = int(id)
            self.__habitacion = int(hab)
            self.__estado = bool(estado)
            self.__paciente = paciente
            self.__diagnostico = str(diag)
            self.__fechaInternacion = fInter
            if(fAlta == 'None'):
                self.__fechaAlta = None
            else:
                self.__fechaAlta = fAlta
    def __str__(self): #premite mostrar ciertos datos de una instancia cama
        text = ''
        if(self.__fechaAlta == None):
            text = 'Paciente: {:10}     Cama: {:2}      Habitacion: {:4}\nDiagnostico: {:10}    Fecha de internacion: {:8}\nFecha de Alta:'.format(self.__paciente, self.__idCama, self.__habitacion, self.__diagnostico, self.__fechaInternacion)
        else:
            text = 'Paciente: {:10}     Cama: {:2}      Habitacion: {:4}\nDiagnostico: {:10}    Fecha de internacion: {:8}\nFecha de Alta: {:8}'.format(self.__paciente, self.__idCama, self.__habitacion, self.__diagnostico, self.__fechaInternacion, self.__fechaAlta)
        return text
    def getPaciente(self): #da el nombre del paciente
        return self.__paciente
    def getDiag(self): #da el diagnóstico del paciente
        return self.__diagnostico
    def getIdCama(self): #da la id de la cama
        return self.__idCama