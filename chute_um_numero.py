import random

class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100

    def Iniciar(self):
        self.GerarUmNumeroAleatorio()
        valor_do_chute = input('Chute um número: ')
        if int(valor_do_chute) > self.valor_aleatorio:
            print('Chute um valor mais baixo')
        elif int(valor_do_chute) < self.valor_aleatorio:
            print('Chute um valor mais alto')

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')
