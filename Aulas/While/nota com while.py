nota = float(input('Qual foi sua nota?'))

while nota < 0 or nota > 10:
    print ('Nota invalida')
    nota = float(input('Digite um valor valido?'))

print ('Valor valido')