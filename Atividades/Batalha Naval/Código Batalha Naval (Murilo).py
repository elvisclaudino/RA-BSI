def geraTabuleiro(linhas,colunas):
    tabuleiro = []
    linha = []
    alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]

    #Ponto possui duas informaçãoes (Jogada e navio)
    ponto = [" M " ,'P1']

    #Laço para gerar tabuleiro de linhas x colunas
    for i in range(linhas+1):
        if i == 0:
            for j in range(colunas+1):
                if j > 0 :
                    linha.append(j)
                else:
                    linha.append('X')

        else:
            for j in range(colunas+1):
                if j == 0 and i > 0:
                    linha.append(alfabeto[i-1])
                else:
                    linha.append(ponto)    
        tabuleiro.append(linha)
        linha = []

    return tabuleiro

def perguntaPosicoes(tabuleiro):

    for perguntas in range(3):
        navio = perguntaNavio(tabuleiro,'Porta avião ' + str(perguntas+1),4,'P')


    
def perguntaNavio(tabuleiro,navio,tamanho,identificador):

    while True:
        print("Informe a posição do navio :",navio, "com tamanho de ", tamanho, "posições")

        posicaoColuna = int(input("Informe a posição da coluna:"))
        posicaoLinha = int(input("Informe a posição da linha:"))

        statusPosicao = verificaPosicao(tabuleiro,posicaoLinha,posicaoColuna,tamanho)

        if statusPosicao :
            for i in range(tamanho):
                tabuleiro[posicaoLinha][posicaoColuna+1][1] = identificador
            return

def verificaPosicao(posicaoLinha,posicaoColuna,tabuleiro,tamanho):
    if posicaoLinha > 20 or posicaoLinha < 0 or  posicaoColuna > 20 or posicaoColuna < 0:
        print("Posição fora dos limites do tabuleiro")
    else:
        for i in range (tamanho):
            if tabuleiro[posicaoLinha][posicaoColuna+1][0] != ' . ':
                return False
            else:
                return True

def imprimeTabuleiro(tabuleiro):
    linha = []
    for i in range(0,20):
        for j in range(0,20):
            if i == 0 or j == 0:
                linha.append(tabuleiro[i][j])
            else:
                if tabuleiro[i][j][0] != ' A ':
                    linha.append(tabuleiro[i][j][0])
                else:
                    linha.append(tabuleiro[i][j][1])
    
        print(linha)
        linha = []

print("Jogo Batalha Naval")

tabuleiro = geraTabuleiro(20,20)

imprimeTabuleiro(tabuleiro)

perguntaPosicoes(tabuleiro)