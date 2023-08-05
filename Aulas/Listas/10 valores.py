vetor = []

for cont in range (10):
    vetor.append(int(input('Digite um número')))

contador = 0

numero = int(input("Insira um número para a localização: "))

while contador < (len(vetor)):
    if numero == (vetor[contador]):
        print ('O número', numero, 'está na', contador, '° posição!')
        break
    contador += 1  

print ('Não localizou')   
