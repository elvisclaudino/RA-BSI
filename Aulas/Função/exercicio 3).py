altura_criancas = []

def media_altura(alturas):
    total = 0
    for cont in alturas:
        total = total + cont
    media_altura = total/5
    return media_altura

def maior_altura(alturas):
    maior = 0

    for cont in range(len(alturas)):
        if maior < alturas[cont]:
            maior = alturas[cont]

    return maior

def menor_altura(alturas):
    menor = alturas[0]

    for cont in range(1, len(alturas)):
        if menor > alturas[cont]:
            menor = alturas[cont]

    return menor

for cont in range (5):
    altura_criancas.append(float(input("Qual a altura")))

media_alturas = media_altura(altura_criancas)
print(media_alturas)

maior_das_alturas = maior_altura(altura_criancas)c
print(maior_das_alturas)

menor_das_alturas = menor_altura(altura_criancas)
print(menor_das_alturas)