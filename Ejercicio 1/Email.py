class correo:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''
    def __init__(self, id = '', dominio = '', tipo = '', contraseña = ''):
        self.__idCuenta = id
        self.__dominio = dominio
        self.__tipoDominio = tipo
        self.__contraseña = contraseña
    def crearCuenta(self, id = 'unknown', dominio = 'unknown', tipo = 'unknown', contraseña = 'unknown'):
        self.__idCuenta = id
        self.__dominio = dominio
        self.__tipoDominio = tipo
        self.__contraseña = contraseña
    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio)
    def getDominio(self):
        return self.__dominio
    def getContraseña(self):
        return self.__contraseña
    def modContraseña(self, contraseña = ''):
        self.__contraseña = contraseña
    def mostrar(self): #muestra el correo y la contraseña
        return '{}@{}.{} Contraseña: {}'.format(self.__idCuenta, self.__dominio, self.__tipoDominio, self.__contraseña)