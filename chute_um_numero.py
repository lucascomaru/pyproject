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
                 [sg.Output(size=(20,10))]
        ]
        #Criar uma Janela
        self.janela = sg.Window('Chute um número! ', Layout=layout)
        #Receber valores
        self.evento, self.valores = self.janela.Read()
        self.valor_do_chute = self.valores['ValorChute']
        #Fazer algo com esses valores
        self.GerarNumeroAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Parabéns, você acertou!! ')
        except:
            print('Por favor, digite apenas números! ')


    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteUmNumero()
chute.Iniciar()
