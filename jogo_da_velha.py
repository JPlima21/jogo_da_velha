from tkinter import *
from tkinter import ttk
import tkinter

# cores
co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 = "#fcfbf7"
fundo = "#3b3b3b"  # preta / black

# Cirando a janela principal
window = Tk()
window.title('')
window.geometry('260x370')
window.resizable(height=False, width=False)
window.configure(bg=fundo)


# Dividindo a janela em dois frames
frame_cima = Frame(window, width=240, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(window, width=240, height=300, bg=fundo, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando o frame cima
# player X
app_x = Label(frame_cima, text='X', height=1, relief='flat',
              anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text='Player 1', height=1, relief='flat',
              anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=25, y=65)
app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat',
                     anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_x_pontos.place(x=85, y=20)

# separaçãseparador
app_separador = Label(frame_cima, text=':', height=1, relief='flat',
                      anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co0)
app_separador.place(x=113, y=9)

# player O
app_o = Label(frame_cima, text='O', height=1, relief='flat',
              anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_o.place(x=175, y=10)
app_o = Label(frame_cima, text='Player 2', height=1, relief='flat',
              anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_o.place(x=178, y=65)
app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat',
                     anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_o_pontos.place(x=135, y=20)


# Criando a logica do jogo
player_1 = 'X'
player_2 = 'O'

score_1 = 0
score_2 = 0

tabela = [['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3']]

jogando = 'X'
jogar = ''
contador = 0


def iniciar():
    # para controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar

        # comparando o valor recebido
        if i == '1':
            # verificando se a possiçâo esta vazia ou não
            if button1['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button1['fg'] = cor
                button1['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

        # comparando o valor recebido
        if i == '2':
            # verificando se a possiçâo esta vazia ou não
            if button2['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button2['fg'] = cor
                button2['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

         # comparando o valor recebido
        
        # comparando o valor recebido
        if i == '3':
            # verificando se a possiçâo esta vazia ou não
            if button3['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button3['fg'] = cor
                button3['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

        # comparando o valor recebido
        if i == '4':
            # verificando se a possiçâo esta vazia ou não
            if button4['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button4['fg'] = cor
                button4['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')


          # comparando o valor recebido
        
        # comparando o valor recebido
        if i == '5':
            # verificando se a possiçâo esta vazia ou não
            if button5['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button5['fg'] = cor
                button5['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

        # comparando o valor recebido
        if i == '6':
            # verificando se a possiçâo esta vazia ou não
            if button6['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button6['fg'] = cor
                button6['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

         # comparando o valor recebido
        
        # comparando o valor recebido
        if i == '7':
            # verificando se a possiçâo esta vazia ou não
            if button7['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button7['fg'] = cor
                button7['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

        # comparando o valor recebido
        if i == '8':
            # verificando se a possiçâo esta vazia ou não
            if button8['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button8['fg'] = cor
                button8['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')

        # comparando o valor recebido
        if i == '9':
            # verificando se a possiçâo esta vazia ou não
            if button9['text'] == '':
                if jogando == 'X':
                    cor = co7
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcar aquela poisição da tabela
                #  com o valor do jogador atual
                button9['fg'] = cor
                button9['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem esta jogando, pra trocar de turno
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'jogador 1'

                else:
                    jogando = 'X'
                    jogar = 'jogador 2'

                #Contador de pontos
                contador += 1

                #Apos o contador ser maior ou igual a 5,
                #verificar se ouve algum vencedor
                if contador >= 5:
                    #linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!='':
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!='':
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!='':
                        vencedor()

                    #colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0]!='':
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!='':
                        vencedor()

                    #diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2]!='':
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!='':
                        vencedor(jogando)
                    
                    #empate
                    if contador >= 9:
                        vencedor('Foi empate')





        print(i)
    # decidir o vencedor

    def vencedor(i):
        global contador_de_rodadas
        global contador
        global jogando
        global tabela
        global score_1
        global score_2

        #limpando o tabuleiro
        button1['text'] = ''
        button2['text'] = ''
        button3['text'] = ''
        button4['text'] = ''
        button5['text'] = ''
        button6['text'] = ''
        button7['text'] = ''
        button8['text'] = ''
        button9['text'] = ''

        button1['state'] = 'disable'
        button2['state'] = 'disable'
        button3['state'] = 'disable'
        button4['state'] = 'disable'
        button5['state'] = 'disable'
        button6['state'] = 'disable'
        button7['state'] = 'disable'
        button8['state'] = 'disable'
        button9['state'] = 'disable'


        #apresentando o vencedor
        app_vencedor = Label(frame_baixo, text='O vencedor é', width=17, relief='flat',anchor='center', font=('Ivy 13 bold'), bg=co1, fg=co2)
        app_vencedor.place(x=45, y=200)

        if i == 'X':
            score_2+=1
            app_vencedor['text'] = 'Player 2 venceu'
            app_o_pontos['text'] = score_2

        if i == 'O':
            score_1+=1
            app_vencedor['text'] = 'Player 1 venceu'
            app_x_pontos['text'] = score_1

        if i == 'Foi empate':
            app_vencedor['text'] = 'Foi um empate'

        def star():
            button1['state'] = 'normal'
            button2['state'] = 'normal'
            button3['state'] = 'normal'
            button4['state'] = 'normal'
            button5['state'] = 'normal'
            button6['state'] = 'normal'
            button7['state'] = 'normal'
            button8['state'] = 'normal'
            button9['state'] = 'normal'

            app_vencedor.destroy()
            b_play.destroy()
            
            # Botão jogar
            b_play = Button(frame_baixo, command=iniciar, text='Play', width=10, height=1, font=(
                'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
            b_play.place(x=85, y=210)

    # para terminar o jogo
    def finalizar():
        pass

    # Configurando o frame baixo
    # linha verticais
    app = Label(frame_baixo, text='', height=23, relief='flat', pady=5, padx=3, anchor='center',
                font=('Ivy 5 bold'),
                bg=co0, fg=co7)
    app.place(x=93, y=30)
    app = Label(frame_baixo, text='', height=23, relief='flat', pady=5, padx=3, anchor='center',
                font=('Ivy 5 bold'),
                bg=co0, fg=co7)
    app.place(x=163, y=30)

    # linhas horizontais
    app = Label(frame_baixo, text='', width=200, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'),
                bg=co0,
                fg=co7)
    app.place(x=30, y=80)
    app = Label(frame_baixo, text='', width=200, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'),
                bg=co0,
                fg=co7)
    app.place(x=30, y=145)

    # linha 1
    button1 = Button(frame_baixo, command=lambda: controlar('1'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button1.place(x=35, y=25)

    button2 = Button(frame_baixo, command=lambda: controlar('2'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button2.place(x=106, y=25)

    button3 = Button(frame_baixo, command=lambda: controlar('3'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button3.place(x=177, y=25)

    # linha 2
    button4 = Button(frame_baixo, command=lambda: controlar('4'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button4.place(x=35, y=91)

    button5 = Button(frame_baixo, command=lambda: controlar('5'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button5.place(x=106, y=91)

    button6 = Button(frame_baixo, command=lambda: controlar('6'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button6.place(x=177, y=91)

    # linha 3
    button7 = Button(frame_baixo, command=lambda: controlar('7'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button7.place(x=35, y=156)

    button8 = Button(frame_baixo, command=lambda: controlar('8'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button8.place(x=106, y=156)

    button9 = Button(frame_baixo, command=lambda: controlar('9'), text='', width=3, font=(
        'Ivy 19 bold'), overrelief=RIDGE, relief='flat', bg=fundo, fg=co7)
    button9.place(x=177, y=156)


# Botão jogar
b_play = Button(frame_baixo, command=iniciar, text='Play', width=10, height=1, font=(
    'Ivy 10 bold'), overrelief=RIDGE, relief='raised', bg=fundo, fg=co0)
b_play.place(x=85, y=210)


window.mainloop()
