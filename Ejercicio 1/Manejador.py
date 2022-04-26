from Email import correo
import csv
class control:
    __lista = []
    __documento = []
    def __init__(self):
        self.__lista = []
    def punto1(self, id = '', dominio = '', tipo = ''):
        unCorreo = correo()
        unCorreo.crearCuenta(id, dominio, tipo)
        #print(unCorreo.retornaEmail())
        self.__lista.append(unCorreo)
    def punto2uno(self, correo = '', contraseña = ''): #modifica la contraseña de la lista de instancias
        for i in self.__lista:
            if(correo == i.retornaEmail()):
                i.modContraseña(contraseña)
    def punto2dos(self, correo = '', contraseña = ''): #modifica la contraseña de la lista del documento
        for i in self.__documento:
            if(correo == i.retornaEmail()):
                i.modContraseña(contraseña)
    def punto3(self, email = ''):
        unCorreo = correo()
        parte1 = email.split("@")
        parte2 = parte1[1].split(".")
        unCorreo.crearCuenta(parte1[0], parte2[0], parte2[1])
        self.__lista.append(unCorreo)
    def punto4(self):
        band = True
        documento = open('Correos.csv')
        reader = csv.reader(documento, delimiter = ';')
        for fila in reader:
            if(band == True):
                band = False
            else:
                parte1 = fila[0].split("@")
                parte2 = parte1[1].split(".")
                unCorreo = correo()
                unCorreo.crearCuenta(parte1[0], parte2[0], parte2[1])
                self.__documento.append(unCorreo)
    def punto5(self):
        band = False
        if(self.__documento):
            band = True
        return band
    def buscar(self, correo = ''): #cuenta las veces que un correo se encuentra repetido en la lista del documento
        contador = 0
        for i in self.__documento:
            if(correo == i.retornaEmail()):
                contador += 1
        return contador
    def verificar(self, correo = ''): #compara el correo ingresado con los correos existentes
        band = False
        for i in self.__lista:
            if(correo == i.retornaEmail()):
                band = True
        return band
    def verificarContra1(self, correo = '', contraseña = ''):
        band = False
        for i in self.__lista:
            if(correo == i.retornaEmail()):
                if(contraseña == i.getContraseña()):
                    band = True
        return band
    def verificarContra2(self, correo = '', contraseña = ''):
        band = False
        for i in self.__documento:
            if (correo == i.retornaEmail()):
                if (contraseña == i.getContraseña()):
                    band = True
        return band
    def mostrar(self):  #muestra los correos registrados
        print('----LISTA DE INSTANCIA----')
        for i in self.__lista:
            print(i.mostrar())
        print('----LISTA DE DOCUMENTO----')
        for i in self.__documento:
            print(i.mostrar())
    def verDocumento(self):
        texto = ''
        if(self.__documento):
            texto = 'LISTO'
        else:
            texto = 'NO LISTO'
        return texto

    #Testeo de creación de instacias de email
    def tester(self, id, dominio, tipo, contra):
        unCorreo = correo(id, dominio, tipo, contra)
