VALOR_PEDAGIO_CARRO = 3.5
VALOR_PEDAGIO_MOTO = 2.75

VALOR_KM_CARRO= 1.5
VALOR_KM_MOTO = 1.0

class Automovel :
    """Uma locação"""
    def __init__(self,montadora,modelo):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = False
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f"Automovel {self.montadora} {self.modelo} aduquirido pela Locadora")

    def alugar(self,nome_cliente):
        """"Cliente pegou o carro"""

        if not self.alugado:
            self.alugado = True
            self.nome_cliente = nome_cliente
            print(f'Automovel {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}')

    def devolver(self):
        """Cliente devolveu o carro"""

        if self.alugado :
            self.alugado = False
            print(f'O automovel {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}')
        else:
            print('O carro precisa estar alugado pra poder devolvelo')
        
    def gerar_fatura(self,numero_pedagios,km_rodado):
        """Classe Abstrata"""

        raise NotImplementedError


class Carro(Automovel):
    """Carro"""
    def __init__(self, montadora, modelo):
        super().__init__(montadora, modelo)
        print('Carro adiquirido')

    def gerar_fatura(self,numero_pedagios,km_rodado):
        """Fazendo a fatura"""

        if self.alugado:
            self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_CARRO + km_rodado * VALOR_KM_CARRO
            print(f'Fatura do {self.montadora} {self.modelo} , valor de R$ {self.valor_fatura}')
        else:
            print(f'Esse {self.modelo} não foi alugado')


class Moto(Automovel):
    """Moto"""
    def __init__(self, montadora, modelo):

        super().__init__(montadora, modelo)
        print('Pegou um carro')

    def gerar_fatura(self,numero_pedagios,km_rodado):

        if self.alugado:
            self.valor_fatura = numero_pedagios * VALOR_PEDAGIO_MOTO + km_rodado * VALOR_KM_MOTO
            print(f'Fatura do {self.montadora} {self.modelo} , valor de R$ {self.valor_fatura}')
        else:
            print(f'Esse {self.modelo} não foi alugado')

uno = Carro('Fiat','Uno')
#x300 = Moto('Honda','xre300',True)

uno.gerar_fatura(numero_pedagios=1,km_rodado=300)
