numero_votantes = int(input('Quantas pessoas irão votar?'))
votos_candidato1 = 0
votos_candidato2 = 0

for cont in range (numero_votantes):

    print ('=-' * 12)

    print ('[1] para candidato 1')
    print ('[2] para candidato 2')

    print ('=-' * 12)

    voto = int(input('Qual seu voto?'))
    if voto == 1:
        votos_candidato1 += 1
    else:
        votos_candidato2 += 1

print ('=-' * 12)

print ('votos candidato 1:', votos_candidato1)
print ('votos candidato 2:', votos_candidato2)