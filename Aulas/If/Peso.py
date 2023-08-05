peso = float(input('Qual seu peso'))

if peso < 50:
    print ('Categoria: Palha')
elif peso < 60:
    print ('Categoria: Pluma')
elif peso < 76:
    print ('Categoria: Leve')
elif peso < 88:
    print ('Categoria: Pesado')
else:
    print ('Categoria: Super pesado')