tempo_total_pequeno = 0
tempo_total_medio = 0
tempo_total_grande = 0
cont_pequeno = 0
cont_medio = 0
cont_grande = 0
viagem = 1

for cont in range (10):
    print (viagem, '° viagem')
    print ('Selecione o tamanho do avião:')
    print ('[1] Avião pequeno')
    print ('[2] Avião médio')
    print ('[3] Avião grande')
    tamanho_aviao = int(input('Qual o tamanho?'))

    if tamanho_aviao == 1:
        tempo_aviao_pequeno = int(input('Qual foi o tempo do avião pequeno?'))
        tempo_total_pequeno += tempo_aviao_pequeno
        cont_pequeno += 1
    if tamanho_aviao == 2:
        tempo_aviao_medio = int(input('Qual foi o tempo do avião médio?'))
        tempo_total_medio += tempo_aviao_medio
        cont_medio += 1
    if tamanho_aviao == 3:
        tempo_aviao_grande = int(input('Qual foi o tempo do avião grande?'))
        tempo_total_grande += tempo_aviao_grande
        cont_grande += 1
    
    viagem += 1

media_aviao_pequeno = tempo_total_pequeno/cont_pequeno
print ('Quantidade aviao pequeno:', cont_pequeno)
print ('media aviao pequeno:', media_aviao_pequeno)

media_aviao_medio = tempo_total_medio/cont_medio
print ('Quantidade aviao medio:', cont_medio)
print ('media aviao medio:', media_aviao_medio)

media_aviao_grande = tempo_total_grande/cont_grande
print ('quantidade aviao grande:', cont_grande)
print ('media aviao grande:', media_aviao_grande)

