from random import randint

while True:
    print ('''Modos de jogo:
[ 1 ] ➝  HUMANO X HUMANO 👨VS👨
[ 2 ] ➝  HUMANO X COMPUTADOR 👨VS💻
[ 3 ] ➝  COMPUTADOR X COMPUTADOR 💻VS💻
[ 4 ] ➝  Encerrar o jogo...''')
    modo_jogo = int(input('Qual modo deseja jogar?'))
    while modo_jogo >= 5 or modo_jogo <=0:
        print ("Escolha uma opção válida!")
        modo_jogo = int(input('Qual modo deseja jogar?'))
    
    if modo_jogo == 1:
        ponto_jogador1 = 0
        ponto_jogador2 = 0
        while (ponto_jogador1 <2 and ponto_jogador2 <2):
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
            if jogador1 == 0: #Jogador 1 jogou PEDRA
                print ('-=' * 12)
                print ('Jogador1 jogou PEDRA 🗿')
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram PEDRA 🗿')
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print ('Jogador2 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print ('Jogador1 venceu! PEDRA 🗿 ganha de TESOURA ✂️')
            elif jogador1 == 1: #Jogador 1 jogou PAPEL
                print ('-=' * 12)
                print ('Jogador1 jogou PAPEL 📃')
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print('Jogador1 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram PAPEL 📃')
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print('Jogador2 venceu! TESOURA ✂️ ganha de PAPEL 📃')
            elif jogador1 == 2: #--Jogardor 1 jogou TESOURA--
                print ('-=' * 12)
                print ('Jogador2 jogou TESOURA ✂️')
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print('Jogardor2 venceu! PEDRA 🗿 ganha de TESOURA ✂️')
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print('Jogador1 venceu! TESOURA ✂️ ganha de PAPEL 📃')
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram TESOURA ✂️')
            print ('Jogador1', ponto_jogador1, 'x', ponto_jogador2, 'Jogador2')
            if ponto_jogador1 == 2:
                print('Parabéns, Jogador1 ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_jogador2 == 2:
                print('Parabéns, Jogador2 ganhou o jogo!')
                print ('-=' * 12)
        print ('''Escolha...
[0] ➝  Para voltar ao menu...
[1] ➝  Para encerrar o jogo...''')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12)
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12)
            break

    elif modo_jogo == 2:  
        ponto_jogador = 0
        ponto_computador = 0
        while (ponto_jogador <2 and ponto_computador <2):
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
            if computador == 0: #--Computador jogou PEDRA--
                print ('-=' * 12)
                print ('Computador jogou PEDRA 🗿')
                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram PEDRA 🗿')
                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_jogador += 1
                    print ('Jogador venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif jogador == 2:
                    print ('Jogador jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_computador += 1
                    print ('Computador venceu! PEDRA 🗿 ganha de TESOURA ✂️')
            elif computador == 1: #--Computador jogou PAPEL--
                print ('-=' * 12)
                print ('Computador jogou PAPEL 📃')
                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_computador += 1
                    print ('Computador venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12)
                    print ('Empate! Ambos jogaram PAPEL 📃')
                elif jogador == 2:
                    print ('Jogador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_jogador += 1
                    print ('Jogador venceu! TESOURA ✂️ ganha de PAPEL 📃')
            elif computador == 2: #--Computador jogou TESOURA--
                print ('-=' * 12)
                print ('Computador jogou TESOURA ✂️')
                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_jogador += 1
                    print('Jogardor venceu! PEDRA 🗿 ganha de TESOURA ✂️')
                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_computador += 1
                    print ('Computador venceu! TESOURA ✂️ ganha de PAPEL 📃')
                elif jogador == 2:
                    print ('Jogador jogou TESOURA ✂️')
                    print ('-=' * 12)
                    print ('Empate! Ambos jogaram TESOURA ✂️')
            print ('Jogador', ponto_jogador, 'x', ponto_computador, 'Computador')
            if ponto_jogador == 2:
                print('Parabéns, Jogador ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_computador == 2:
                print('Computador ganhou o jogo!')
                print ('-=' * 12)
        print ('''Escolha...
[0] ➝  Para voltar ao menu...
[1] ➝  Para encerrar o jogo...''')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12)
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12)
            break
   
    elif modo_jogo == 3:    
        ponto_computador1 = 0
        ponto_computador2 = 0
        while (ponto_computador1 <2 and ponto_computador2 <2):
            computador1 = randint(0, 2)
            computador2 = randint(0, 2)
            print ('-=' * 12)
            print ('''Opções:
[ 0 ] ➝  PEDRA 🗿
[ 1 ] ➝  PAPEL 📃
[ 2 ] ➝  TESOURA ✂️''')
            if computador1 == 0: #--Computador jogou PEDRA--
                print ('-=' * 12)
                print ('Computador1 jogou PEDRA 🗿')
                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    print ('Empate! Ambos jogaram PEDRA 🗿')
                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_computador2 += 1
                    print ('Computador2 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_computador1 += 1
                    print ('Computador1 venceu! PEDRA 🗿 ganha de TESOURA ✂️')
            elif computador1 == 1: #--Computador jogou PAPEL--
                print ('-=' * 12)
                print ('Computador1 jogou PAPEL 📃')
                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_computador1 += 1
                    print ('Computador1 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    print ('Empate! Ambos jogaram PAPEL 📃')
                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    ponto_computador2 += 1
                    print ('Computador2 venceu! TESOURA ✂️ ganha de PAPEL 📃')
            elif computador1 == 2: #--Computador jogou TESOURA--
                print ('-=' * 12)
                print ('Computador1 jogou TESOURA ✂️')
                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_computador2 += 1
                    print('Computador2 venceu! PEDRA 🗿 ganha de TESOURA ✂️')
                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_computador1 += 1
                    print ('Computador1 venceu! TESOURA ✂️ ganha de PAPEL 📃')
                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂️')
                    print ('-=' * 12)
                    print ('Empate! Ambos jogaram TESOURA ✂️')
            print ('Computador1', ponto_computador1, 'x', ponto_computador2, 'Computador2')
            if ponto_computador1 == 2:
                print('Computador1 ganhou o jogo!')
                print ('-=' * 12)
            elif ponto_computador2 == 2:
                print('Computador2 ganhou o jogo!')
                print ('-=' * 12)
        print ('''Escolha...
[0] ➝  Para voltar ao menu...
[1] ➝  Para encerrar o jogo...''')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12)
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12)
            break
    
    elif modo_jogo == 4:
        print ('-=' * 12)
        print ('''Deseja mesmo encerrar o jogo?
[0] ➝  Para voltar ao jogo...
[1] ➝  Para encerrar...''')
        print ('-=' * 12)
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)
        if encerrar_jogo == 0:
            print ('Voltando ao  jogo...')
            print ('-=' * 12)
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12)
            break