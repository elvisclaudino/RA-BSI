voto_um = 0
voto_dois = 0
cont_voto = 0

votantes = int(input('Qual a quantidade de votantes?'))
for cont in range (votantes):
    print (cont_voto, '° voto')
    print ('Opções:')
    print ('[1] para candidato 1')
    print ('[2] para candidato 2')
    voto = int(input('Qual o seu voto'))
    while voto > 2 or voto < 0:
        voto = int(input('Digite um voto valido:'))    
    if voto == 1:
        voto_um += 1
    else:
        voto_dois += 1
    cont_voto += 1

print ('Quantidade de voto do candidato um:', voto_um)
print ('Quantidade de voto do candidato dois:', voto_dois)
if voto_um > voto_dois:
    print ('O candidato 1 ganhou')
elif voto_um == voto_dois:
    print ('Empate!')
else:
    print ('O candidato 2 ganhou')