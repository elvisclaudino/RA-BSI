cont = 0
maior = 0
menor = 0
while cont < 5:
    numero = int(input('Qual número deseja?'))
    cont += 1
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
print (numero)