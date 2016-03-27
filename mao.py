from baralho import Baralho, Carta

class Mao(object):
    
    def __init__(self):
        self.cartas = [None, None, None, None, None]
        #self.cartas = [Carta(10,'d'), Carta(11,'d'), Carta(12,'d'), Carta(13,'d'), Carta(14,'d')]
        self.baralho = None
    
    def devolver(self):
        self.cartas = [None, None, None, None, None]
    
    def embaralhar(self):
        self.baralho = Baralho()
    
    def pegar_cartas(self):
        for i in range(5):
            if not self.cartas[i]:
                self.cartas[i] = self.baralho.puxar()
    
    def combinacao(self):
        if None in self.cartas:
            return None
        self.cartas.sort(key=lambda x: x.valor)
        if self.royal_flush():
            return 0
        elif self.straight_flush():
            return 1
        elif self.four_of_a_kind():
            return 2
        elif self.full_house():
            return 3
        elif self.flush():
            return 4
        elif self.straight():
            return 5
        elif self.three_of_a_kind():
            return 6
        elif self.two_pair():
            return 7
        elif self.pair():
            return 8
        else:
            return None
        
    def royal_flush(self):
        if self.cartas[0].valor == 10 and self.straight_flush():
            return True
        return False

    def straight_flush(self):
        return self.straight() and self.flush()

    def four_of_a_kind(self):
        l = list(map(lambda x: x.valor, self.cartas))
        s = list(set(l))
        m = max(map(lambda x: l.count(x), s))
        if m == 4:
            return True
        return False
    
    def full_house(self):
        l = list(map(lambda x: x.valor, self.cartas))
        s = list(set(l))
        l = list(map(lambda x: l.count(x), s))
        l.sort()
        if l == [2,3]:
            return True
        return False

    def flush(self):
        n = len(list(set(map(lambda x: x.naipe, self.cartas))))
        if n == 1:
            return True
        return False
    
    def straight(self):
        for i in range(len(self.cartas)-1):
            if self.cartas[i].valor+1 != self.cartas[i+1].valor:
                return False
        return True

    def three_of_a_kind(self):
        l = list(map(lambda x: x.valor, self.cartas))
        s = list(set(l))
        m = max(map(lambda x: l.count(x), s))
        if m == 3:
            return True
        return False
    
    def two_pair(self):
        l = list(map(lambda x: x.valor, self.cartas))
        s = list(set(l))
        m = list(map(lambda x: l.count(x), s))
        if max(m) == 2 and m.count(2) == 2:
            return True
        return False

    def pair(self):
        l = list(map(lambda x: x.valor, self.cartas))
        s = list(set(l))
        m = max(map(lambda x: l.count(x), s))
        if m == 2:
            return True
        return False
