from Manejador import manejador

class menu:
    __opcion = None
    __funcion = None
    __control = None
    def __init__(self):
        self.__opcion = {1: self.mostrar, 2: self.promedio, 3: self.listar, 4: self.salir}
        self.__control = manejador()
        d = self.__control.lecturaLista()
        self.__control.crearLista(d)
    def opcion(self, op):
        self.__funcion = self.__opcion.get(op)
        if self.__funcion:
            self.__funcion()
        else:
            print('ERROR: opcion invalida')
            input()
    def mostrar(self): #muestran los datos máximos y mínimos del mes
        #Temperatura máxima y mínima
        print('Temperatura:')
        lista = self.__control.punto1Max(0)
        print('----TEMPERATURA MAXIMA----\nDia: {:2} - Hora: {:2}hrs - Temperatura: {}°C'.format(lista[0], lista[1],
                                                                                             lista[2]))
        lista = self.__control.punto1Min(0)
        print('----TEMPERATURA MINIMA----\nDia: {:2} - Hora: {:2}hrs - Temperatura: {}°C'.format(lista[0], lista[1],
                                                                                             lista[2]))
        #Humedad máxima y mínima
        print('Humedad:')
        lista = self.__control.punto1Max(1)
        print('----HUMEDAD MAXIMA----\nDia: {:2} - Hora: {:2}hrs - Humedad: {}%'.format(lista[0], lista[1], lista[2]))
        lista = self.__control.punto1Min(1)
        print('----HUMEDAD MINIMA----\nDia: {:2} - Hora: {:2}hrs - Humedad: {}%'.format(lista[0], lista[1], lista[2]))
        #Presión máxima y mínima
        print('Presion atmosferica: ')
        lista = self.__control.punto1Max(2)
        print('----PRESION MAXIMA----\nDia: {:2} - Hora: {:2}hrs - Presion: {}Pa'.format(lista[0], lista[1], lista[2]))
        lista = self.__control.punto1Min(2)
        print('----PRESION MINIMA----\nDia: {:2} - Hora: {:2}hrs - Presion: {}Pa'.format(lista[0], lista[1], lista[2]))
    def promedio(self): #se calcula y muestra el promedio de las temperaturas en el mes por hora
        hora = 1
        print('Promedio de temperatura mensual:')
        lista = self.__control.punto2()
        for temp in lista:
            print('Hora: {}hrs - Temperatura: {:.2f}°C'.format(hora, temp))
            hora += 1
    def listar(self): #se muestra los datos según el día ingresado
        dia = int(input('Ingrese dia: '))
        lista = self.__control.punto3(dia-1)
        hora = 0
        print('Lista de registros:\nHora     Temperatura     Humedad     Presion')
        for registro in lista:
            print('{:5}       {}'.format(hora, registro))
            hora += 1
    def salir(self):
        print('FINALIZANDO...')
        input()