frutas = ["laranja", "maça", "pera", "banana", "kiwi", "maca", "banana"]
numeros = [1, 2, 3]

frutas.append('abacate')

lista = []
lista.append(10)
lista.append(20)

for cont in range(len(lista)):
    print (lista[cont])

frutas.insert(1,'manga')
frutas.remove('maça')
for cont in range(len(frutas)):
    print (frutas[cont])