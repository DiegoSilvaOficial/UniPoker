from tkinter import *

from util import ToggleButton, ButtonRadio, RadioGroup, Table, Util
from mao import Mao

class Jogo(Tk):

    def __init__(self,parent, player, seed):
        Tk.__init__(self,parent)
        self.credito = 1000.0
        self.player = player
        self.parent = parent
        self.passo = 0
        self.initialize()

    def initialize(self):

        #Configs
        self.resizable(False, False)
        self.geometry('{}x{}'.format(800, 600))
        self.configure(background='#2F736A')

        self.mao = Mao()
        self.images = []
        self.labels = []
        self.holds = []

        self.create_labels()
        self.draw_images()
        t = Table(self, Util.maos, 10, 85)
        t.draw()

        self.label_credito = Label(self, text="Crédito: $ %.2f" % self.credito, bg='#2F736A', fg="#FFFFFF", font=("Mono", 15))
        self.label_credito.place(x=790, y=10, anchor=NE)
        
        self.label_player = Label(self, text="Player: {}".format(self.player), bg='#2F736A', fg="#FFFFFF", font=("Mono", 15))
        self.label_player.place(x=10, y=10)
        
        self.label_paid = Label(self, bg='#2F736A', fg="#FFFFFF", font=("Mono", 11))
        self.label_paid.place(x=10, y=50)
        
        self.label_bet = Label(self, bg='#2F736A', fg="#FFFFFF", font=("Mono", 11))
        self.label_bet.place(x=10, y=575, anchor=SW)
        
        self.r1 = ButtonRadio(self, text="$ 0,25")
        self.r1.place(x=285, y=585, width=100, height=40,anchor=SE)
        self.r1.select()
        
        self.r2 = ButtonRadio(self, text="$ 1,00")
        self.r2.place(x=435, y=585, width=100, height=40,anchor=SE)
        
        self.r3 = ButtonRadio(self, text="$ 5,00")
        self.r3.place(x=585, y=585, width=100, height=40,anchor=SE)
        
        self.rg = RadioGroup(self.draw_bet)
        self.rg.add(self.r1, 0.25)
        self.rg.add(self.r2, 1.0)
        self.rg.add(self.r3, 5.0)
        
        self.x1 = ButtonRadio(self, text="1")
        self.x1.place(x=325, y=60, height=20, width=85)
        self.x1.select()
        
        self.x2 = ButtonRadio(self, text="2")
        self.x2.place(x=420, y=60, height=20, width=85)
        
        self.x3 = ButtonRadio(self, text="3")
        self.x3.place(x=515, y=60, height=20, width=85)
        
        self.x4 = ButtonRadio(self, text="4")
        self.x4.place(x=610, y=60, height=20, width=85)
        
        self.x5 = ButtonRadio(self, text="5")
        self.x5.place(x=705, y=60, height=20, width=85)

        self.rx = RadioGroup(self.draw_bet)
        self.rx.add(self.x1, 1)
        self.rx.add(self.x2, 2)
        self.rx.add(self.x3, 3)
        self.rx.add(self.x4, 4)
        self.rx.add(self.x5, 5)
        
        self.draw_bet()
        self.draw_paid(0.0)
        
        self.btn_deal = Button(self, text="Deal", command=self.deal, highlightbackground='#000', activebackground="#111", activeforeground="#DDD", relief=FLAT, bg='#333', fg="#DDD", font=("Mono", 15))
        self.btn_deal.place(x=785, y=585, width=100, height=40,anchor=SE)
        
    def deal(self):
        if self.passo == 0:
            self.credito -= (self.rx.selected()*self.rg.selected())
            self.draw_credit()
            self.destroy_images()
            self.mao.embaralhar()
            self.mao.pegar_cartas()
            self.draw_images()
            self.create_holds()
            self.rg.toggle_lock()
            self.rx.toggle_lock()
            self.passo+=1
        elif self.passo == 1:
            for i in range(5):
                if not self.holds[i].value:
                    self.mao.cartas[i] = None
            self.destroy_images()
            self.mao.pegar_cartas()
            self.destroy_holds()
            self.destroy_images()
            self.draw_images()
            retorno = self.mao.combinacao()
            if retorno != None:
                t = Util.maos[retorno][0]
                multiplo = Util.maos[retorno][self.rx.selected()]
                valor = self.rg.selected()
                total = (valor*multiplo)
                self.credito += total
                self.draw_paid(float(total))
                self.draw_credit()
            else:
                t = "No Win"
            self.l = Label(self, text=t,bg='#2F736A', fg="#FFFFFF", font=("Mono", 15))
            self.l.place(relx=0.5, y=30, anchor=CENTER, width=300, height=50)
            self.passo += 1
        elif self.passo == 2:
            self.l.destroy()
            self.draw_paid(0.0)
            self.rg.toggle_lock()
            self.rx.toggle_lock()
            self.mao.devolver()
            self.destroy_images()
            self.draw_images()
            self.passo = 0
            
    
    def draw_credit(self):
        self.label_credito.config(text="Money: $ %.2f" % self.credito)
        
    def draw_bet(self):
        self.label_bet.configure(text="Bet:  $ %.2f" % (self.rg.selected() * self.rx.selected()))
    
    def draw_paid(self, valor):
        self.label_paid.configure(text="Paid: $ %.2f" % valor)
    
    def create_labels(self):
        x = 10
        for i in range(5):
            label = Label(self, bg='#2F736A')
            label.place(x=x, y=320, width=140, height=194)
            self.labels.append(label)
            x += 160

    def draw_images(self):
        x = 10
        for i in range(5):
            card = self.mao.cartas[i]
            if card:
                self.images.append(PhotoImage(file="imagens/{}/{}.png".format(card.naipe,card.valor)))
            else:
                self.images.append(PhotoImage(file="imagens/back.png"))
            self.labels[i].configure(image=self.images[i])

            x += 160
    def destroy_images(self):
        self.images = []
        
    def create_holds(self):
        x = 40
        for i in range(5):
            hold = ToggleButton(self)
            hold.configure(command=hold.toggle)
            hold.place(x=x, y=490, width=80, height=30)
            self.holds.append(hold)
            x += 160
    def destroy_holds(self):
        for hold in self.holds:
            hold.destroy()
        self.holds = []
        
