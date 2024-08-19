from random import randrange

class Celular:
    """Classe de celular"""

    def __init__(self,fabricante,modelo,tela,memoria,camera,bateria):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = 0
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = False

    def ligar_tela(self):
        """Ligar a tv"""
        self.tela_ligada = True

    def charge_phone(self):
        """Coloca carga no celular"""
        self.armazenamento = randrange(1,101)
        return print(f"A bateria esta com car de {self.armazenamento}")

androidCelular = Celular(fabricante='Samsung',modelo='A21',tela='13P',
                         memoria='12g',camera=2,bateria='25h')

print(androidCelular.tela_ligada)
androidCelular.ligar_tela()
print(androidCelular.tela_ligada)

print(androidCelular.armazenamento)
androidCelular.charge_phone()
print(androidCelular.armazenamento)