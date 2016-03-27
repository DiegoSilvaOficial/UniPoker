import os
import csv

class Persistencia(object):

    arquivo = None
    
    def __init__(self, arquivo):
        self.arquivo = os.path.abspath(arquivo)
        if not os.access(arquivo, os.F_OK):
            raise IOError("Arquivo {} não encontrado".format(arquivo))
        if not os.access(arquivo, os.R_OK):
            raise IOError("Arquivo {} não pode ser lido".format(arquivo))

    def escrever(self, ranking):
        try:
            with open(self.arquivo, 'w') as f:
                fieldnames = ['nome', 'credito', 'seed']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for i in ranking:                
                    writer.writerow({'nome': i[0], 'credito': i[1], 'seed':i[2]})
        except IOError as e:
            print("Não foi possível escrever no arquivo {}".format(arquivo))
        finally:
            f.close()

    def ler(self):
        try:
            with open(self.arquivo) as f:
                reader = csv.reader(f)
                return list(reader)
        except IOError as e:
            print("Não foi possível abrir o arquivo {}".format(arquivo))
        finally:
            f.close()
