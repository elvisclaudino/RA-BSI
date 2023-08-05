def somar_valores(valor1, valor2):
    soma = valor1 + valor2
    return soma

def divisao_valores(valor1, valor2):
    if valor2 != 0:
        divisao =  valor1 / valor2
        return divisao
    return False

def multiplicacao_valores(valor1, valor2):
    multiplicar = valor1 * valor2
    return multiplicar

def subtracao_valores(valor1, valor2):
    subtrair = valor1 - valor2
    return subtrair
    
print('Selecione qual operação deseja: ')
print('[1] Soma')
print('[2] Divisão')
print('[3] Multiplicação')
print('[4] Subtração')
operação = int(input('Qual deseja? '))

valor_um = float(input('Qual seu primeiro valor?'))
valor_dois = float(input('Qual seu segundo valor?'))

if operação == 1:
    total_soma = somar_valores(valor_um, valor_dois)
    print(total_soma)

elif operação == 2:
    total_divisao = divisao_valores(valor_um, valor_dois)
    print(total_divisao)

elif operação == 3:
    total_multiplicar = multiplicacao_valores(valor_um, valor_dois)
    print(total_multiplicar)

else:
    total_subtracao = subtracao_valores(valor_um, valor_dois)
    print(total_subtracao)