from tkinter import *

class Util(object):

    dict_cartas = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}
    dict_naipes = {"d":"Diamonds", "h":"Hearts", "c":"Clubs", "s":"Spades"}
    
    maos = [["Royal Flush", 250, 500, 750, 1000, 5000],
            ["Straight Flush", 50, 100, 150, 200, 250],
            ["Four of a Kind", 20, 40, 60, 80, 100],
            ["Full House", 7, 14, 21, 28, 35],
            ["Flush", 5, 10, 15, 20, 25],
            ["Straight", 4, 8, 12, 16, 20],
            ["Three of a Kind", 3, 6, 9, 12, 15],
            ["Two Pair", 2, 4, 6, 8, 10],
            ["Jacks or Better", 1, 2, 3, 4, 5]]
    
class Table(object):
    def __init__(self,pai, dados, x, y):
        self.pai = pai
        self.dados = dados
        self.x = x
        self.y = y
        
    def draw(self):
        for i in range(len(self.dados)):
            x = self.x
            for j in range(len(self.dados[i])):
                if j == 0:
                    color = "yellow"
                    width = 305
                else:
                    color = "#CCC"
                    width = 85
                f = Frame(self.pai, height=20, width=width)
                f.pack_propagate(0) # don't shrink
                f.place(x=x, y=self.y)
                label = Label(f, text=self.dados[i][j], bg="#333", fg=color, font=("Mono",12))
                label.pack(fill=BOTH, expand=1)
                x += width+10
            self.y += 25

class RadioGroup(object):
    
    def __init__(self, atualize):
        self.radios = []
        self.values = []
        self.atualize = atualize
    
    def selected(self):
        for i in range(len(self.radios)):
            if self.radios[i].selected:
                return self.values[i]
        return None
    
    def add(self, radio, value):
        radio.configure(command=self.comando(radio))
        self.radios.append(radio)
        self.values.append(value)
        
    def comando(self,radio):
        def retorno():
            if not radio.selected:
                for i in self.radios:
                    if i.selected:
                        i.deselect()
                radio.select()
                self.atualize()
        return retorno
        

class ButtonRadio(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.selected = False
        self['activeforeground'] = "#111"
        self['activebackground'] = "#BBB"
        self['highlightbackground'] = '#AAA'
        self['bg'] = '#DDD'
        self['fg'] = '#333'
        self['font'] = ("Mono")
        self['relief'] = FLAT
    
    def select(self):
        self.selected = True
        self['activeforeground'] = "#DDD"
        self['activebackground'] = "#333"
        self['highlightbackground'] = '#333'
        self['fg'] = '#DDD'
        self['bg'] = '#333'
    
    def deselect(self):
        self.selected = False
        self['activeforeground'] = "#111"
        self['activebackground'] = "#BBB"
        self['highlightbackground'] = '#AAA'
        self['bg'] = '#DDD'
        self['fg'] = '#333'

class ToggleButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.value = False
        self['text'] = "Release"
        self['activeforeground'] = "#111"
        self['activebackground'] = "#BBB"
        self['highlightbackground'] = '#AAA'
        self['bg'] = '#DDD'
        self['fg'] = '#333'
        self['font'] = ("Mono")
        self['relief'] = FLAT
        
    def toggle(self):
        if self.value:
            self['text'] = "Release"
            self['activeforeground'] = "#111"
            self['activebackground'] = "#BBB"
            self['highlightbackground'] = '#AAA'
            self['bg'] = '#DDD'
            self['fg'] = '#333'
        else:
            self['text'] = "Hold"
            self['activeforeground'] = "#DDD"
            self['activebackground'] = "#111"
            self['highlightbackground'] = '#333'
            self['fg'] = '#DDD'
            self['bg'] = '#333'
        self.value = not self.value
