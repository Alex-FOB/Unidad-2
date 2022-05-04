class conjunto:
    __lista = []
    def __init__(self, lista = []):
        self.__lista = lista
    def __str__(self):
        return '{}'.format(self.__lista)
    def __add__(self, other):
        lista = []
        lista = self.__lista.copy()
        for i in other.getLista():
            if(i not in lista):
                lista.append(i)
        return conjunto(lista)
    def __sub__(self, other):
        lista = []
        lista = self.__lista.copy()
        for i in other.getLista():
            if(i in lista):
                lista.remove(i)
        return conjunto(lista)
    def __eq__(self, other):
        band = True
        lista = other.getLista() #hacemos una copia de la otra lista
        lista.sort() #se ordena el conjunto
        i = 0
        if(len(self.__lista) == len(lista)):
            while not band:
                i += 1
                if(self.__lista[i] != lista[i]):
                    band = False
        else:
            band = False
        return band
    def getLista(self):
        return self.__lista