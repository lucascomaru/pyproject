import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para do dado? '
        #layout

        layout = [
            [sg.Text('Jogar o dado?')]
            [sg.Button('sim'), sg.Button('não')]
        ]
        #criação de janela
        janela = sg.Window('Simulador de Dado', Layout=layout)
        #ler os valores da tela
        self.eventos, self.valores = janela.Read()
        #fazer algo com esses valores
    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim':
                self.GerarValorDoDado()
            elif resposta == 'não':
                print('Agradecemos sua participação')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()

