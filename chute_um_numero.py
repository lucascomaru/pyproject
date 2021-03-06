import random
import PySimpleGUI as sg
class ChuteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #Layaout
        layout = [[sg.Text('Seu chute',size=(39,0))],
                 [sg.Input(size=(18,0), key='ValorChute')],
                 [sg.Button('Chutar!')],
                 [sg.Output(size=(39,10))]
        ]
        #Criar uma Janela
        self.janela = sg.Window('Chute um número! ', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber valores
                self.evento, self.valores = self.janela.read()
                # Fazer algo com esses valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns, você acertou!! ')
                            break
        except:
            print('Por favor, digite apenas números! ')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()
