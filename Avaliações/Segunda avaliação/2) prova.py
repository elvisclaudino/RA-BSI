# Váriavel da lista do salário durante um ano
salario_mensal = []
# Váriavel da lista dos salários menores que mil reais
menores_que_mil = []

# Função que analisa quais valores são menores que mil reais
def valores_menores_que_mil():
    # Lê do teclado o salario mensal durante um ano (12 meses)
    for meses in range(12):
        print(20 * '=-')
        print('Qual foi seu salário no', meses+1, '° mês do ano?')
        salario = float(input('Digite seu salário: '))
        # Enquanto o valor digitador for negativo, será lido do teclado um novo valor até que o mesmo seja positivo
        while salario < 0:
            salario = float(input('Digite um valor positivo: '))
        salario_mensal.append(salario)

    print(20 * '=-')
    print('Valores abaixo de R$1000,00')
    # Percorre a lista de salario mensal inteira e identifica os valores menores que mil reais
    for cont in range(len(salario_mensal)):
        # Se o valor lido for menor que mil reais, será adicionado a outra lista
        if salario_mensal[cont] < 1000:
            menores_que_mil.append(salario_mensal[cont])
    # Retorna a lista dos valores menores que mil reais
    return menores_que_mil

print(valores_menores_que_mil())