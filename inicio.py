from tkinter import *

class Inicio(Tk):

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.protocol("WM_DELETE_WINDOW", sys.exit)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.geometry('{}x{}'.format(400, 230))
        self.configure(background='#2F736A')
        
        self.label_nome = Label(self, text="Nome", bg='#2F736A', fg="#FFFFFF", font=("Mono", 15))
        self.label_nome.place(x=40, y=35)
        
        self.label_seed = Label(self, text="Seed", bg='#2F736A', fg="#FFFFFF", font=("Mono", 15))
        self.label_seed.place(x=40, y=95)
        
        self.box_nome = Entry(self, font=("Mono", 15), bg="#333", fg="#DDD", relief=FLAT,highlightbackground='#000')
        self.box_nome.place(x=120, y=35, height=30)
        self.box_nome.focus_set()
        self.box_nome.bind("<Return>", self.enter)

        self.box_seed = Entry(self, font=("Mono", 15), bg="#333", fg="#DDD", relief=FLAT,highlightbackground='#000')
        self.box_seed.place(x=120, y=95, height=30)
        self.box_seed.bind("<Return>", self.enter)
        
        self.ok = Button(self, text="OK", command=self.comando,highlightbackground='#000', activebackground="#111", activeforeground="#DDD", relief=FLAT, bg='#333', fg="#DDD", font=("Mono", 15))
        self.ok.place(x=150, y=160, width=100, height=40)
        self.ok.bind("<Return>", self.enter)
        
    def comando(self):
        if len(self.box_nome.get()) > 0 and len(self.box_seed.get()) > 0:
            self.seed = self.box_seed.get()
            self.nome = self.box_nome.get()
            self.destroy()
        
    def enter(self, event):
        self.comando()
