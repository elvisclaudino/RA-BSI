from pickle import TRUE
from random import randint

while True:
    print ('''Modos de jogo:
[ 1 ] ➝  HUMANO X HUMANO 👨VS👨
[ 2 ] ➝  HUMANO X COMPUTADOR 👨VS💻
[ 3 ] ➝  COMPUTADOR X COMPUTADOR 💻VS💻
[ 4 ] ➝  Encerrar o jogo...''')
    modo_jogo = int(input('Qual modo deseja jogar?'))
    while modo_jogo >= 5:
        print ("Escolha uma opção válida!")
        modo_jogo = int(input('Qual modo deseja jogar?'))
    
    if modo_jogo == 1:
        ponto_jogador1 = 0
        ponto_jogador2 = 0
        while (ponto_jogador1 <3 and ponto_jogador2 <3):
            itens = ('Pedra', 'Papel', 'Tesoura')
            print ('-=' * 12)
            print ('''Opções:
[ 0 ] ➝  PEDRA 🗿
[ 1 ] ➝  PAPEL 📃
[ 2 ] ➝  TESOURA ✂️''')
            jogador1 = int(input('JOGADOR 1: Qual será sua jogada?'))
            while jogador1 >= 3:
                print ("Faça uma jogada válida")
                jogador1 = int(input('Qual será sua jogada?'))
            jogador2 = int(input('JOGADOR 2: Qual será sua jogada?'))
            while jogador2 >= 3:
                print ("Faça uma jogada válida")
                jogador2 = int(input('Qual será sua jogada?'))
            print ('-=' * 12)
            print ('Jogador1 jogou {}'.format(itens[jogador1]))
            print ('Jogador2 jogou {}'.format(itens[jogador2]))
            print ('-=' * 12)
            if jogador1 == 0: #Jogador 1 jogou PEDRA
                if jogador2 == 0:
                    print('Empate! Ambos jogaram', (itens[jogador1]), '!')
                elif jogador2 == 1:
                    ponto_jogador2 += 1
                    print('Jogador2 venceu!', (itens[jogador2]), 'ganha de', (itens[jogador1]))
                elif jogador2 == 2:
                    ponto_jogador1 += 1
                    print('Jogardor1 venceu!', (itens[jogador1]), 'ganha de', (itens[jogador2]))
            elif jogador1 == 1: #Jogador 1 jogou PAPEL
                if jogador2 == 0:
                    ponto_jogador1 += 1
                    print('Jogador1 venceu!', (itens[jogador1]), 'ganha de', (itens[jogador2]))
                elif jogador2 == 1:
                    print('Empate! Ambos jogaram', (itens[jogador1]), '!')
                elif jogador2 == 2:
                    ponto_jogador2 += 1
                    print('Jogador2 venceu!', (itens[jogador2]), 'ganha de', (itens[jogador1]))
            elif jogador1 == 2: #--Jogardor 1 jogou TESOURA--
                if jogador2 == 0:
                    ponto_jogador2 += 1
                    print('Jogardor2 venceu!', (itens[jogador2]), 'ganha de', (itens[jogador1]))
                elif jogador2 == 1:
                    ponto_jogador1 += 1
                    print('Jogador1 venceu!', (itens[jogador1]), 'ganha de', (itens[jogador2]))
                elif jogador2 == 2:
                    print('Empate! Ambos jogaram', (itens[jogador1]), '!')
            print ('Jogador1', ponto_jogador1, 'x', ponto_jogador2, 'Jogador2')
            if ponto_jogador1 == 3:
                print('Parabéns, Jogador1 ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_jogador2 == 3:
                print('Parabéns, Jogador2 ganhou o jogo!')
                print ('-=' * 12)

    elif modo_jogo == 2:  
        ponto_jogador = 0
        ponto_computador = 0
        while (ponto_jogador <3 and ponto_computador <3):
            itens = ('Pedra', 'Papel', 'Tesoura')
            computador = randint(0, 2)
            print ('-=' * 12)
            print ('''Opções:
[ 0 ] ➝  PEDRA 🗿
[ 1 ] ➝  PAPEL 📃
[ 2 ] ➝  TESOURA ✂️''')
            jogador = int(input('Qual será sua jogada?'))
            while jogador >= 3:
                print ("Faça uma jogada válida")
                jogador = int(input('Qual será sua jogada?'))
            print ('-=' * 12)
            print ('Computador jogou {}'.format(itens[computador]))
            print ('Jogador jogou {}' .format(itens[jogador]))
            print ('-=' * 12)
            if computador == 0: #--Computador jogou PEDRA--
                if jogador == 0:
                    print('Empate! Ambos jogaram', (itens[jogador]), '!')
                elif jogador == 1:
                    ponto_jogador += 1
                    print('Você Venceu!', (itens[jogador]), 'ganha de', (itens[computador]))
                elif jogador == 2:
                    ponto_computador += 1
                    print('Você perdeu!', (itens[computador]), 'ganha de', (itens[jogador]))
            elif computador == 1: #--Computador jogou PAPEL--
                if jogador == 0:
                    ponto_computador += 1
                    print('Você perdeu!', (itens[computador]), 'ganha de', (itens[jogador]))
                elif jogador == 1:
                    print('Empate! Ambos jogaram', (itens[jogador]), '!')
                elif jogador == 2:
                    ponto_jogador += 1
                    print('Você venceu!', (itens[jogador]), 'ganha de', (itens[computador]))
            elif computador == 2: #--Computador jogou TESOURA--
                if jogador == 0:
                    ponto_jogador += 1
                    print('Você venceu!', (itens[jogador]), 'ganha de', (itens[computador]))
                elif jogador == 1:
                    ponto_computador += 1
                    print('Você perdeu!', (itens[computador]), 'ganha de', (itens[jogador]))
                elif jogador == 2:
                    print('Empate! Ambos jogaram', (itens[jogador]), '!')
            print ('Jogador', ponto_jogador, 'x', ponto_computador, 'Computador')
            if ponto_jogador == 3:
                print('Parabéns, Jogador ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_computador == 3:
                print('Computador ganhou o jogo!')
                print ('-=' * 12)
    
    elif modo_jogo == 3:    
        ponto_computador1 = 0
        ponto_computador2 = 0
        while (ponto_computador1 <3 and ponto_computador2 <3):
            itens = ('Pedra', 'Papel', 'Tesoura')
            computador1 = randint(0, 2)
            computador2 = randint(0, 2)
            print ('-=' * 12)
            print ('''Opções:
[ 0 ] ➝  PEDRA 🗿
[ 1 ] ➝  PAPEL 📃
[ 2 ] ➝  TESOURA ✂️''')
            print ('-=' * 12)
            print ('Computador1 jogou {}'.format(itens[computador1]))
            print ('Computador2 jogou {}' .format(itens[computador2]))
            print ('-=' * 12)
            if computador1 == 0: #--Computador jogou PEDRA--
                if computador2 == 0:
                    print('Empate! Ambos jogaram', (itens[computador1]), '!')
                elif computador2 == 1:
                    ponto_computador2 += 1
                    print('Computador2 venceu!', (itens[computador2]), 'ganha de', (itens[computador1]))
                elif computador2 == 2:
                    ponto_computador1 += 1
                    print('Computador1 venceu!', (itens[computador1]), 'ganha de', (itens[computador2]))
            elif computador1 == 1: #--Computador jogou PAPEL--
                if computador2 == 0:
                    ponto_computador1 += 1
                    print('Computador1 venceu!', (itens[computador1]), 'ganha de', (itens[computador2]))
                elif computador2 == 1:
                    print('Empate! Ambos jogaram', (itens[computador1]), '!')
                elif computador2 == 2:
                    ponto_computador2 += 1
                    print('Computador2 venceu!', (itens[computador2]), 'ganha de', (itens[computador1]))
            elif computador1 == 2: #--Computador jogou TESOURA--
                if computador2 == 0:
                    ponto_computador2 += 1
                    print('Computador2 venceu!', (itens[computador2]), 'ganha de', (itens[computador1]))
                elif computador2 == 1:
                    ponto_computador1 += 1
                    print('Computador1 venceu!', (itens[computador1]), 'ganha de', (itens[computador2]))
                elif computador2 == 2:
                    print('Empate! Ambos jogaram', (itens[computador1]), '!')
            print ('Computador1', ponto_computador1, 'x', ponto_computador2, 'Computador2')
            if ponto_computador1 == 3:
                print('Computador1 ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_computador2 == 3:
                print('Computador2 ganhou o jogo!')
                print ('-=' * 12)