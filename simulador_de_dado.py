import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para do dado? '
        #layout

        self.layout = [
            [sg.Text('Jogar o dado?')]
            [sg.Button('sim'), sg.Button('não')]
        ]

    def Iniciar(self):
        # criação de janela
        self.janela = sg.Window('Simulador de Dado', Layout=self.layout)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        # fazer algo com esses valores

        resposta = input(self.mensagem)
        while True:
           try:
                if self.eventos == 'sim':
                    self.GerarValorDoDado()
                elif self.eventos == 'não':
                    print('Agradecemos sua participação')
                else:
                    print('Agradecemos sua participação! ')
           except:
                print('Ocorreu um erro ao receber sua resposta')


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()

