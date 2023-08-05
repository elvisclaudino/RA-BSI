nLinhas = 3
nColunas = 4
notas = [0] * nLinhas

for linha in range(nLinhas):
  notas[linha] = [0] * nColunas

for linha in range(nLinhas):
  for coluna in range(nColunas):
    notas[linha][coluna] = float(input('Digite uma nota: '))
    print(notas)
    
for linha in range(nLinhas):
  soma = 0
  for coluna in range(nColunas):
    soma = soma + notas[linha][coluna]
    media = soma/nColunas
  print('Media = ', media)