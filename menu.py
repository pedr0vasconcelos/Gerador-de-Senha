from string import ascii_letters as a
from string import digits as n
from string import punctuation as p
from random import sample as al
import PySimpleGUI as sg

j = ''.join
def criar_gerador():
    sg.theme('DarkBlue4')

    linha = [        
        [sg.Push(), sg.Slider((1, 50), orientation='horizontal', key='-DGT-', default_value=22), sg.Push()],  
        [sg.Push(), sg.Text(j(al(a+n+p, 22)), key='-SENHA-', size=(50,1))],
        [sg.Push(), sg.Button('Gerar Senha'),sg.Button('Copiar Senha'), sg.Push()]
    ]

    layout = [
        [sg.Frame('Escolha o Tamanho da sua Senha!', layout=linha, key='container')]
    ]
    
    return sg.Window('Gerador de Senhas', layout=layout, finalize=True)

janela = criar_gerador()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Gerar Senha':
        senha_tamanho = int(values['-DGT-'])
        resultado = j(al(a+n+p, senha_tamanho))
        janela['-SENHA-'].update(resultado)
    elif event == 'Copiar Senha':
        sg.clipboard_set(janela['-SENHA-'].get())