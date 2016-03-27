import random, sys

from persistencia import Persistencia
from ranking import Ranking

from inicio import Inicio
from jogo import Jogo

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError('É necessário informar um arquivo como parametro')
        p = Persistencia(sys.argv[1])
        
        inicio = Inicio(None)
        inicio.title('UniPoker')
        inicio.mainloop()
        
        player = inicio.nome.title()
        seed = inicio.seed
        
        random.seed(seed)

        while True:
            jogo = Jogo(None, player, seed)
            jogo.title('UniPoker')
            jogo.mainloop()
            
            credito = jogo.credito
            
            r = Ranking(None, player, credito, seed)
            r.title('Ranking')
            r.mainloop()
            
            if not r.reini:
                break
    except Exception as e:
        print(e)
        sys.exit()
