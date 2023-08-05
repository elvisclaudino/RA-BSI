numero = int(input('Insira um número'))
soma = numero
for cont in range (numero-1,0,-1):
    soma = soma * cont
print ('o fatorial de', numero, 'é', soma)