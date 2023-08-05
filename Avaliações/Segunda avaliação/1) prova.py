# váriaveis globais para gerar a  matriz 3x7 (casos de covid em 3 bairros por 7 dias)
bairros = 3
dias_semana = 7
covid = [0] * bairros

# Função que analisa qual foi o maior valor na quinta posição da matriz (sexta-feira)
def maior_numero_de_casos_sexta_feira(matriz):
    # gerando matriz
    for linha in range (bairros):
        matriz[linha] = [0] * dias_semana

    # Enquanto o número de bairros for menor que 3 irá para o próximo for
    for bairro in range(3):
        print(20 * '=-')
        # Enquanto o número de dias for menor do que 7, acionara o input para ser adicionado um número de casos de covid na matriz
        for dia in range(7):
            print('Quantos casos teve no BAIRRO', bairro+1, 'no', dia+1, '° DIA da semana?')
            # Adiciona o número de casos lido pelo teclado na matriz
            matriz[bairro][dia] = int(input('Digite o número de casos: '))
            # Enquanto o valor digitado for negativo, será lido novamente até ser digitado um valor positivo
            while matriz[bairro][dia] < 0:
                print(12 * '=-')
                matriz[bairro][dia] = int(input('Insira um valor positivo: '))

    # igualando o maior número à zero, para que possa ser substituido
    maior = 0
    # Ira passar pelas 3 linhas
    for cont in range(3):
        # Se o novo valor for maior que o antigo, sera o novo valor da variável maior
        if maior < matriz[cont][5]:
            maior = matriz[cont][5]
    
    print(20 * '=-')
    # Se o maior for igual a outro maior, irá retornar 'Igual"
    if maior == matriz[0][5] and maior == matriz[1][5] or maior == matriz[0][5] and maior == matriz[2][5] or maior == matriz[1][5] and maior == matriz[2][5]:
        return('Iguais')

    # Se o maior número for a quinta coluna da primeira linha, retornara 'Bairro 1'
    elif maior == matriz[0][5]:
        return 'Bairro 1 foi o que teve mais casos na sexta-feira'
    # Se o maior número for a quinta coluna da segunda linha, retornara 'Bairro 2'
    elif maior == matriz[1][5]:
        return 'Bairro 2 foi o que teve mais casos na sexta-feira'
    # Senão retornara 'Bairro 3'
    else:
        return 'Bairro 3 foi o que teve mais casos na sexta-feira'

# Printa a função, colocando a matriz covid como parâmetro
print(maior_numero_de_casos_sexta_feira(covid))