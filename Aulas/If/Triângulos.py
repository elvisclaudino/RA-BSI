ladoA = int(input('Insira o lado A:'))
ladoB = int(input('Insira o lado B:'))
ladoC = int(input('Insira o lado C:'))

if (ladoA < (ladoB + ladoC)) and (ladoB < (ladoA + ladoC)) and (ladoC < (ladoA + ladoB)):
    if (ladoA == ladoB) and (ladoB == ladoC):
        print ('Triangulo equilatero')
    elif (ladoA == ladoB) or (ladoB == ladoC) or (ladoA == ladoC):
        print ('Triangulo isosceles')
    else:
        print ('Triangulo escaleno')
else:
    print ('Esses numeros nao formam um triangulo')