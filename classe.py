class Celula:
    """ Dosstring, serpe pra dizer oque a classe vai fazer"""
    def __init__(self, marca, memoria):
        self.marca = marca
        self.memoria = memoria

caro = Celula(marca='samsung', memoria='8gb')
print(caro.marca)
print(caro.memoria)
