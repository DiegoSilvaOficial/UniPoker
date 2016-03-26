from util import Util

import random

naipes = ["d", "h", "c", "s"]

valores = [i for i in list(range(2,15))]

class Carta(object):

    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __repr__(self):
        valor = Util.dict_cartas.get(self.valor,self.valor)
        naipe = Util.dict_naipes.get(self.naipe,self.naipe)
        return "%s of %s" % (valor, naipe)
    
    def __lt__(self, other):
        return self.valor < other

    def __gt__(self, other):
        return self.valor > other

class Baralho(object):
    
    cartas = []
    
    def __init__(self):
        [[self.cartas.append(Carta(valor, naipe)) for valor in valores] for naipe in naipes]

    def puxar(self):
        print(len(self.cartas))
        return self.cartas.pop(random.randint(0, len(self.cartas)-1))
