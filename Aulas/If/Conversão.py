print ('O que você quer converter?')
print ('[1] Dólar para Real')
print ('[2] Real para Dolar')
conversao = int(input('Sua escolha:'))

if conversao == 1:
    dolar = float(input('Quantos dólares você quer converter?'))
    valor_real = dolar * 4.62
    print ('Você tem:' ,valor_real, 'R$')

elif conversao == 2:
    real = float(input('Quantos reais você quer converter?'))
    valor_dolar = real / 4.62
    print ('Você tem:', valor_dolar, '$')