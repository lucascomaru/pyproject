import random

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100

    def Iniciar(self):
        self.GerarUmNumeroAleatorio()