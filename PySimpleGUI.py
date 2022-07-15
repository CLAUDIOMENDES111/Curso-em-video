import PySimpleGUI as sg


sg.theme("Reddit")

layout = [
    [Text('Usuário'), Input(key='usuario')],
    [Text('Senha')], Input(key='senha', password_char='*')
    [Button('ENTRAR')]

]

janela = window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == WINDOW_CLOSED:
        break
    if eventos =='ENTRAR':
        if valores['usuario'] =='CLAUDIO' and valores['senha'] == '123456':
            print('Deu certo')

