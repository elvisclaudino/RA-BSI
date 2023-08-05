from random import randint

#Dados estatisticos do Jogo
vitorias_jogador1 = 0           #Numero de vitorias do Jogador 1
vitorias_jogador2 = 0           #Numero de vitorias do Jogador 2
derrotas_jogador1 = 0           #Numero de derrotas do Jogador 1
derrotas_jogador2 = 0           #Numero de derrotas do Jogador 2
jogadas_ganhas_jogador1 = 0     #Numero jogadas ganhas do Jogador 1
jogadas_ganhas_jogador2 = 0     #Numero jogadas ganhas do Jogador 2
jogadas_perdidas_jogador1 = 0   #Numero jogadas perdidas do Jogador 1
jogadas_perdidas_jogador2 = 0   #Numero jogadas perdidas do Jogador 2
jogadas_empatadas_jogador1 = 0  #Numero jogadas empatadas do Jogador 1
jogadas_empatadas_jogador2 = 0  #Numero jogadas empatadas do Jogador 2

while True: #Jogador informa o modo de jogo selecionado
    print ('Modos de jogo:')
    print ('[ 1 ] ➝  HUMANO X HUMANO 👨VS👨')
    print ('[ 2 ] ➝  HUMANO X COMPUTADOR 👨VS💻')
    print ('[ 3 ] ➝  COMPUTADOR X COMPUTADOR 💻VS💻')
    print ('[ 4 ] ➝  Encerrar o jogo...')
    modo_jogo = int(input('Qual modo deseja jogar?'))

    #Equanto os jogadores nao informarem o modo de jogo correto
    while modo_jogo >= 5 or modo_jogo <=0:
        print ("Escolha uma opção válida!")
        modo_jogo = int(input('Qual modo deseja jogar?'))

    #Se o modo de jogo for 1
    if modo_jogo == 1:
        ponto_jogador1 = 0
        ponto_jogador2 = 0

        #Enquanto nenhum dos jogadores venceu a melhor de 3
        while (ponto_jogador1 <2 and ponto_jogador2 <2):
            print ('-=' * 12)
            print ('Opções:')
            print ('[ 0 ] ➝  PEDRA 🗿')
            print ('[ 1 ] ➝  PAPEL 📃')
            print ('[ 2 ] ➝  TESOURA ✂')
            jogador1 = int(input('Jogador1: Qual será sua jogada?'))

            #Equanto o jogador 1 não informou uma jogada correta
            while jogador1 > 2 or jogador1 < 0:
                print ("Faça uma jogada válida")
                jogador1 = int(input('Qual será sua jogada?'))
            #É informado as opções de jogo novamente
            print ('Opções:')
            print ('[ 0 ] ➝  PEDRA 🗿')
            print ('[ 1 ] ➝  PAPEL 📃')
            print ('[ 2 ] ➝  TESOURA ✂')
            jogador2 = int(input('Jogador2: Qual será sua jogada?'))

             #Equanto o jogador 2 não informou uma jogada correta
            while jogador2 > 2:
                print ("Faça uma jogada válida")
                jogador2 = int(input('Qual será sua jogada?'))

            #Se o jogador1 jogou pedra
            if jogador1 == 0: #Jogador 1 jogou PEDRA
                print ('-=' * 12)
                print ('Jogador1 jogou PEDRA 🗿')

                #Se o jogador2 jogou pedra
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram PEDRA 🗿')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                #Se o jogador2 jogou papel
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print ('Jogador2 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                #Se o jogador2 jogou Tesoura
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print ('Jogador1 venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

            #Se o jogador1 jogou papel
            elif jogador1 == 1: #Jogador 1 jogou PAPEL
                print ('-=' * 12)
                print ('Jogador1 jogou PAPEL 📃')

                #Se o jogador2 jogou pedra
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print('Jogador1 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

                #Se o jogador2 jogou papel
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram PAPEL 📃')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                #Se o jogador2 jogou Tesoura
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print('Jogador2 venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

            #Se o jogador1 jogou tesoura
            elif jogador1 == 2: #--Jogardor 1 jogou TESOURA--
                print ('-=' * 12)
                print ('Jogador2 jogou TESOURA ✂')

                #Se o jogador2 jogou pedra
                if jogador2 == 0:
                    print ('Jogador2 jogou PEDRA 🗿')
                    print ('-=' * 12)
                    ponto_jogador2 += 1
                    print('Jogardor2 venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                #Se o jogador2 jogou papel
                elif jogador2 == 1:
                    print ('Jogador2 jogou PAPEL 📃')
                    print ('-=' * 12)
                    ponto_jogador1 += 1
                    print('Jogador1 venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

                #Se o jogador2 jogou Tesoura
                elif jogador2 == 2:
                    print ('Jogador2 jogou TESOURA ✂')
                    print ('-=' * 12)
                    print('Empate! Ambos jogaram TESOURA ✂')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

            #Informa placar
            print ('Jogador1', ponto_jogador1, 'x', ponto_jogador2, 'Jogador2')

            #Informa se o jogador 1 ganhou
            if ponto_jogador1 == 2:
                print('Parabéns, Jogador1 ganhou o jogo!')
                print ('-=' * 12)
                vitorias_jogador1+=1 #Incrementa vitorias do jogador 1
                derrotas_jogador2+=1 #Incrementa derrotas do jogador 2

            #Informa se o jogador 2 ganhou
            elif ponto_jogador2 == 2:
                print('Parabéns, Jogador2 ganhou o jogo!')
                print ('-=' * 12)
                vitorias_jogador2+=1 #Incrementa vitorias do jogador 2
                derrotas_jogador1+=1 #Incrementa derrotas do jogador 1

        #Informa menu para escolha de continuar ou encerrar
        print ('Escolha...')
        print ('[0] ➝  Para voltar ao menu...')
        print ('[1] ➝  Para encerrar o jogo...')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)

        #Se o usuário quiser continuar jogando
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12)

        #Se o usuário quiser encerrar
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12)
            break

    #Se o modo de jogo for 2
    elif modo_jogo == 2:
        ponto_jogador = 0
        ponto_computador = 0
        #Aparece as opções de jogo para o jogador digitar
        while (ponto_jogador <2 and ponto_computador <2):
            computador = randint(0, 2)
            print ('-=' * 12)
            print ('Opções:')
            print('[ 0 ] ➝  PEDRA 🗿')
            print('[ 1 ] ➝  PAPEL 📃')
            print('[ 2 ] ➝  TESOURA ✂')
            jogador = int(input('Qual será sua jogada?'))
            #Caso o jogador digite uma jogada inválida
            while jogador >= 3:
                print ("Faça uma jogada válida")
                jogador = int(input('Qual será sua jogada?'))

            if computador == 0: #--Computador jogou PEDRA--
                print ('-=' * 12) #Divisória
                print ('Computador jogou PEDRA 🗿')

                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    print('Empate! Ambos jogaram PEDRA 🗿')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    ponto_jogador += 1
                    print ('Jogador venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2


                elif jogador == 2:
                    print ('Jogador jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    ponto_computador += 1
                    print ('Computador venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

            elif computador == 1: #--Computador jogou PAPEL--
                print ('-=' * 12) #Divisória
                print ('Computador jogou PAPEL 📃')

                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    ponto_computador += 1
                    print ('Computador venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    print ('Empate! Ambos jogaram PAPEL 📃')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                elif jogador == 2:
                    print ('Jogador jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    ponto_jogador += 1
                    print ('Jogador venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

            elif computador == 2: #--Computador jogou TESOURA--
                print ('-=' * 12) #Divisória
                print ('Computador jogou TESOURA ✂')

                if jogador == 0:
                    print ('Jogador jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    ponto_jogador += 1
                    print('Jogardor venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

                elif jogador == 1:
                    print ('Jogador jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    ponto_computador += 1
                    print ('Computador venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                elif jogador == 2:
                    print ('Jogador jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    print ('Empate! Ambos jogaram TESOURA ✂')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

            print ('Jogador', ponto_jogador, 'x', ponto_computador, 'Computador')

            if ponto_jogador == 2:
                print('Parabéns, Jogador ganhou o jogo!')
                print ('-=' * 12) #Divisória
                vitorias_jogador1+=1 #Incrementa vitorias do jogador 1
                derrotas_jogador2+=1 #Incrementa derrotas do jogador 2

            elif ponto_computador == 2:
                print('Computador ganhou o jogo!')
                print ('-=' * 12) #Divisória
                vitorias_jogador2+=1 #Incrementa vitorias do jogador 2
                derrotas_jogador1+=1 #Incrementa derrotas do jogador 1

        #Informa menu para escolha de continuar ou encerrar
        print ('Escolha...')
        print ('[0] ➝  Para voltar ao menu...')
        print ('[1] ➝  Para encerrar o jogo...')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12)
        #Caso seja escolhido encerrar o jogo
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12) #Divisória

        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12) #Divisória
            break

    #Se o modo de jogo for 3
    elif modo_jogo == 3:
        ponto_computador1 = 0
        ponto_computador2 = 0
        while (ponto_computador1 <2 and ponto_computador2 <2):
            computador1 = randint(0, 2)
            computador2 = randint(0, 2)
            print ('-=' * 12) #Divisória
            print ('Opções:') #As opções de jogo são novamente apresentadas
            print ('[ 0 ] ➝  PEDRA 🗿')
            print ('[ 1 ] ➝  PAPEL 📃')
            print ('[ 2 ] ➝  TESOURA ✂')

            if computador1 == 0: #--Computador jogou PEDRA--
                print ('-=' * 12) #Divisória
                print ('Computador1 jogou PEDRA 🗿')

                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    print ('Empate! Ambos jogaram PEDRA 🗿')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    ponto_computador2 += 1
                    print ('Computador2 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    ponto_computador1 += 1
                    print ('Computador1 venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

            elif computador1 == 1: #--Computador jogou PAPEL--
                print ('-=' * 12) #Divisória
                print ('Computador1 jogou PAPEL 📃')

                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    ponto_computador1 += 1
                    print ('Computador1 venceu! PAPEL 📃 ganha de PEDRA 🗿')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    print ('Empate! Ambos jogaram PAPEL 📃')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    ponto_computador2 += 1
                    print ('Computador2 venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

            elif computador1 == 2: #--Computador jogou TESOURA--
                print ('-=' * 12) #Divisória
                print ('Computador1 jogou TESOURA ✂')

                if computador2 == 0:
                    print ('Computador2 jogou PEDRA 🗿')
                    print ('-=' * 12) #Divisória
                    ponto_computador2 += 1
                    print('Computador2 venceu! PEDRA 🗿 ganha de TESOURA ✂')
                    jogadas_ganhas_jogador2+=1      #Incrementa jogadas ganhas do jogador 2
                    jogadas_perdidas_jogador1+=1    #Incrementa jogadas perdidas do jogador 1

                elif computador2 == 1:
                    print ('Computador2 jogou PAPEL 📃')
                    print ('-=' * 12) #Divisória
                    ponto_computador1 += 1
                    print ('Computador1 venceu! TESOURA ✂ ganha de PAPEL 📃')
                    jogadas_ganhas_jogador1+=1      #Incrementa jogadas ganhas do jogador 1
                    jogadas_perdidas_jogador2+=1    #Incrementa jogadas perdidas do jogador 2

                elif computador2 == 2:
                    print ('Computador2 jogou TESOURA ✂')
                    print ('-=' * 12) #Divisória
                    print ('Empate! Ambos jogaram TESOURA ✂')
                    jogadas_empatadas_jogador1+=1   #Incrementa número de jogadas empatadas jogador 1
                    jogadas_empatadas_jogador2+=1   #Incrementa número de jogadas empatadas jogador 2

            print ('Computador1', ponto_computador1, 'x', ponto_computador2, 'Computador2')
            if ponto_computador1 == 2:
                print('Computador1 ganhou o jogo!')
                print ('-=' * 12) #Divisória
                vitorias_jogador1+=1 #Incrementa vitorias do jogador 1
                derrotas_jogador2+=1 #Incrementa derrotas do jogador 2

            elif ponto_computador2 == 2:
                print('Computador2 ganhou o jogo!')
                print ('-=' * 12) #Divisória
                vitorias_jogador2+=1 #Incrementa vitorias do jogador 2
                derrotas_jogador1+=1 #Incrementa derrotas do jogador 1
        #Após o termino da partida é pedido para o usuário se o mesmo quer continuar jogando
        print ('Escolha...')
        print ('[0] ➝  Para voltar ao menu...')
        print ('[1] ➝  Para encerrar o jogo...')
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12) #Divisória
        #Caso opte por encerrar o o jogo
        if encerrar_jogo == 0:
            print ('Voltando ao menu...')
            print ('-=' * 12) #Divisória

        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12) #Divisória
            break
        #É pedido ao usuário se o mesmo quer continuar jogando ou encerrar a partida
    elif modo_jogo == 4:
        print ('-=' * 12) #Divisória
        print ('Deseja mesmo encerrar o jogo?')
        print ('[0] ➝  Para voltar ao jogo...')
        print ('[1] ➝  Para encerrar...')
        print ('-=' * 12) #Divisória
        encerrar_jogo = int(input('O que deseja?'))
        print ('-=' * 12) #Divisória
        #Caso opte por encerrar o o jogo
        if encerrar_jogo == 0:
            print ('Voltando ao  jogo...')
            print ('-=' * 12) #Divisória
        elif encerrar_jogo == 1:
            print ('Jogo encerrado!!!')
            print ('-=' * 12) #Divisória
            break

#Calculo percentual das vitórias e jogadas
percentual_vitorias_jogador1 = (100*vitorias_jogador1)/(vitorias_jogador1+vitorias_jogador2)
percentual_vitorias_jogador2 = (100*vitorias_jogador2)/(vitorias_jogador2+vitorias_jogador1)
percentual_jogadas_jogador1 =  (100*jogadas_ganhas_jogador1)/(jogadas_ganhas_jogador1+jogadas_empatadas_jogador1+jogadas_perdidas_jogador1)
percentual_jogadas_jogador2 =  (100*jogadas_ganhas_jogador2)/(jogadas_ganhas_jogador2+jogadas_empatadas_jogador2+jogadas_perdidas_jogador2)

print("O jogador1 teve ",vitorias_jogador1," vitóras com ",jogadas_ganhas_jogador1," jogadas ganhas,", jogadas_empatadas_jogador1 , "jogadas empatadas e", jogadas_perdidas_jogador1," jogadas perdidas.")
print("Tendo um aproveitamento de", percentual_vitorias_jogador1,"% no quesito vitórias e um percentual de", percentual_jogadas_jogador1, "% no quesito jogadas certas")
print ('-=' * 12) #Divisória
print("O jogador2 teve ",vitorias_jogador2," vitóras com ",jogadas_ganhas_jogador2," jogadas ganhas,", jogadas_empatadas_jogador2 , "jogadas empatadas e", jogadas_perdidas_jogador2," jogadas perdidas.")
print("Tendo um aproveitamento de", percentual_vitorias_jogador2,"% no quesito vitórias e um percentual de", percentual_jogadas_jogador2, "% no quesito jogadas certas")