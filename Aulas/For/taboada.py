numero = int(input('Você quer a taboada de que número?'))
taboada = 0
for cont in range (0,11):
    taboada = numero * cont
    print (taboada)
print ('FIM')