alturas = []
total_alturas = 0

for cont in range(5):
    altura = int(input('Insira a altura'))
    alturas.append(altura)
    total_alturas += altura

media = total_alturas/5
print ('A média das alturas são', media)

for cont in range (len(alturas)):
    if alturas[cont] > media:
        print ('Altura acima da média', alturas[cont])
