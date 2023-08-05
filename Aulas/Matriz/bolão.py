nJogadores = 5
nJogos = 3
nTimes = 2

bolao = [0] * nJogadores

for jogador in range(nJogadores):
    bolao[jogador] = [0] * nJogos
    for jogo in range (nJogos):
        bolao[jogador][jogo] = [0] * nTimes

for jogador in range(nJogadores):
    print('Aposta do', jogador, ':')
    for jogo in range(nJogos):
        print('Aposta do jogo ', jogo, ':')
        for time in range(nTimes):
            print('Número de gols do time ', time, ':')
            bolao[jogador][jogo][time] = int(input('Digite o # de gols: '))

print(bolao)