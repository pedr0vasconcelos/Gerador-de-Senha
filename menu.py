from string import ascii_letters as a
from string import digits as n
from string import punctuation as p
from random import sample as al
import PySimpleGUI as sg

j = ''.join
def criar_gerador():
    sg.theme('DarkBlue4')
    layout = [
        [sg.Text(j(al(a+n+p, 22)), key='-SENHA-',size=(25,1))],
        [sg.Button('Gerar Senha'),sg.Button('Copiar Senha')]
    ]

    return sg.Window('Gerador de Senhas', layout=layout, finalize=True)

janela = criar_gerador()

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Gerar Senha':
        resultado = j(al(a+n+p, 22))
        janela['-SENHA-'].update(resultado)
    elif event == 'Copiar Senha':
        sg.clipboard_set(janela['-SENHA-'].get())