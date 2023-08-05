#Dados iniciais
viagem = 1
soma_aviao_pequeno = 0
soma_aviao_medio = 0
soma_aviao_grande = 0

for cont in range (10):    #Até dar o limite de 10 repetições
    print ('=-' * 12)      #Divisória
    print('Tempo da viagem n°:', viagem)    #Em qual viagem está
    aviao_pequeno = float(input('Qual o tempo de voo entre São Paulo e Curitiba de um avião pequeno em minutos?'))  #Ler o tempo em minutos do avião pequeno
    aviao_medio = float(input('Qual o tempo de voo entre São Paulo e Curitiba de um avião médio em minutos?'))  #Ler o tempo em minutos do avião médio
    aviao_grande = float(input('Qual o tempo de voo entre São Paulo e CUritiba de um avião grande em minutos')) #Ler o tempo em minutos do avião grande
    soma_aviao_pequeno += aviao_pequeno     #A soma de todos os valores em minutos do avião pequeno
    soma_aviao_medio += aviao_medio     #A soma de todos os valores em minutos do avião médio
    soma_aviao_grande += aviao_grande   #A soma de todos os valores em minutos do avião grande
    viagem += 1   #O número da viagem
print ('-=' * 12)      #Divisória

media_aviao_pequeno = soma_aviao_pequeno/10     #A soma dos valores do avião pequeno divido pelo número de viagens
print('A viagem do avião pequeno leva em média:', media_aviao_pequeno, 'minutos')   #Imprime a média na tela   

media_aviao_medio = soma_aviao_medio/10     #A soma dos valores do avião médio divido pelo número de viagens
print('A viagem do avião médio leva em média:', media_aviao_medio, 'minutos')   #Imprime a média na tela  

media_aviao_grande = soma_aviao_grande/10     #A soma dos valores do avião grande divido pelo número de viagens
print('A viagem do avião grande leva em média:', media_aviao_grande, 'minutos')     #Imprime a média na tela  

print ('-=' * 12)      #Divisória    