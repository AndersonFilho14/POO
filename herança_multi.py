from random import choice


class Dev:
    '''Dev'''

    def __init__(self,linguagem_pro=None):
        self.linguagem_pro = linguagem_pro
        print(f"Novo desenvolvedor com expertise nas linguagens de :\n\t{self.linguagem_pro}")

    def desenvolver(self):
        '''Codando'''
        print(f'Pssssiuuuuuuuuuuu! Dev codando em {choice(self.linguagem_pro)} ')


class Gerente:
    '''gerente'''

    def __init__(self,softskills=None):
        self.softskills = softskills
        print(f'Novo gerente com softskills \n\t{choice(softskills)} ')

    def gerenciar(self):
        '''Gerente  '''
        print(f'Gerente esta utilizando {choice(self.softskills)} para genrenciar')

class TechLeader(Dev,Gerente):
    '''dev e gerente'''

    def __init__(self, linguagem_pro=None,softskills=None):
        Dev.__init__(self,linguagem_pro)
        Gerente.__init__(self,softskills)

teachLeadr = TechLeader(['C','C++','Python'],['liderança','comunicação'])
teachLeadr.desenvolver()
teachLeadr.gerenciar()
