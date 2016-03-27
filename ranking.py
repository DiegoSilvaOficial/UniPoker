from tkinter import *

from persistencia import Persistencia
from util import Table

#class Player(object):
#    
#    def __init__(self, nome, credito):
#        self.nome = nome
#        self.credito = credito
#    

class Ranking(Tk):
    
    def __init__(self,parent, player, credito, seed):
        Tk.__init__(self,parent)
        self.resizable(False, False)
        self.player = player
        self.credito = credito
        self.seed = seed
        self.parent = parent
        self.reini = False
        self.initialize()
    
    def reinit(self):
        self.reini = True
        self.destroy()
    
    def initialize(self):
        self.geometry('{}x{}'.format(800, 650))
        self.configure(background='#2F736A')
        
        p = Persistencia(sys.argv[1])
        
        lista = p.ler()
        
        lista = list(map(lambda x: [x[0], float(x[1]), x[2]], lista))
        
        lista.append([self.player, self.credito,self.seed])
        
        lista.sort(key=lambda x:x[1])
        
        lista.reverse()
        
        p.escrever(lista[:20])
        
        t = Table(self, p.ler(), 10, 20)
        t.draw(big=True)
        
        self.ok = Button(self, text="Jogar Novamente", command=self.reinit,highlightbackground='#000', activebackground="#111", activeforeground="#DDD", relief=FLAT, bg='#333', fg="#DDD", font=("Mono", 15))
        self.ok.place(x=300, y=530, width=200, height=40)
        self.ok.bind("<Return>", self.enter)
        
        self.ok = Button(self, text="Sair", command=self.comando,highlightbackground='#000', activebackground="#111", activeforeground="#DDD", relief=FLAT, bg='#333', fg="#DDD", font=("Mono", 15))
        self.ok.place(x=350, y=590, width=100, height=40)
        self.ok.bind("<Return>", self.enter)
        
    def comando(self):
        self.destroy()
        
    def enter(self, event):
        self.comando()
