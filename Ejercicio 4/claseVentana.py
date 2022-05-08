class Ventana:
    __título = ''
    __verSupIzq = [] #vertice superior inzquierda
    __verInfDer = [] #vertica inferior derecha
    def __init__(self, titulo = '', sup = [0, 0], inf = [500, 500]):
        self.__título = titulo
        if(sup[0] < inf[0] and sup[1] < inf[1] and sup >= [0, 0] and inf <= [500, 500]):
            self.__verSupIzq = sup
            self.__verInfDer = inf
        else:
            self.__verSupIzq = [0, 0]
            self.__verInfDer = [500, 500]
    def getTitulo(self):
        return self.__título
    def alto(self):
        return self.__verInfDer[0] - self.__verSupIzq[0]
    def ancho(self):
        return self.__verInfDer[1] - self.__verSupIzq[1]
    def mostrar(self): #PREGUNTAR
        print('----{}----\nVertice superior izquierdo: {} - Vertice inferior derecho: {}'.format(self.__título,
                                                                                                  self.__verSupIzq,
                                                                                                  self.__verInfDer))
    def moverDerecha(self, x = 0):
        self.__verSupIzq[0] += x
        self.__verInfDer[0] += x
    def moverIzquierda(self, x = 0):
        self.__verSupIzq[0] -= x
        self.__verInfDer[0] -= x
    def subir(self, y = 0):
        self.__verSupIzq[1] += y
        self.__verInfDer[1] += y
    def bajar(self, y = 0):
        self.__verSupIzq[1] -= y
        self.__verInfDer[1] -= y