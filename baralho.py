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

    def __init__(self):
        self.cartas = [(Carta(valor, 'd')) for valor in valores]
        self.cartas += [(Carta(valor, 'h')) for valor in valores]
        self.cartas += [(Carta(valor, 'c')) for valor in valores]
        self.cartas += [(Carta(valor, 's')) for valor in valores]

    def puxar(self):
        return self.cartas.pop(random.randint(0, len(self.cartas)-1))
