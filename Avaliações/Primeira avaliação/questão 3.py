valor = float(input('Qual o valor do produto?'))    #Ler o valor do produto

while valor < 0:    #Enquanto o valor for negativo
    print ('Insira um valor positivo!')     #Aviso para inserir um valor positivo
    valor = float(input('Qual o valor do produto?'))    #Ler novamente o valor do produto

parcelas = valor/3      #Divião das parcelas

print(valor, 'R$ parcelado em 3x, irá ficar', parcelas, 'R$ por mês')   #Imprime o valor parcelado do produto