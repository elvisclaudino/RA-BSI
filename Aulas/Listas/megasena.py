numeros = []
premiados = [20, 37, 6, 48, 29, 50]
contador = 0
certos = 0
errados = 0

for cont in range (6):
    numeros.append(int(input('Insira um número')))
    print(numeros)

for cont in range (6):
    if numeros[contador] == premiados[contador]:
        certos += 1
    else:
        errados += 1
    contador += 1
    
print('Núimeros certos', certos)
