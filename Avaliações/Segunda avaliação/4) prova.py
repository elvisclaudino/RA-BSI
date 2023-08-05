# Variável global da lista de numero de telefone
numero_telefone = []

# Função que verifica se o DDD é = 41
def verificar_ddd(lista):
    # Enquanto o contador for menor que dez (número de digitos do número de telefone), ira ler um digito ao usuários
    for cont in range(10):
        print(20 * '=-')
        # Se o contador for menor que dois, ira perguntar o ddd do usuários, que no caso são os primeiros dois números
        if cont < 2:
            print(cont+1, '° digito do seu DDD')
            numero = int(input('Insira um DDD (um digito de cada vez, de 0 à 9): '))
            # Enquanto o valor for acima de dois digitos ou o valor for negativo, ira ler novamente outro valor
            while numero > 10 or numero < 0:
                numero = int(input('Insira um dígito de 0 a 9: '))
        # Senão, (contador > 2) ira ler os digitos do número do usuário
        else:
            print(cont-1, '° digito do seu número')
            numero = int(input('Insira seu número (um dígito de cada vez, de 0 à 9): '))
            # Enquanto o valor for acima de dois digitos ou o valor for negativo, ira ler novamente outro valor
            while numero > 10 or numero < 0:
                numero = int(input('Insira um dígito de 0 a 9: '))
        #Após passar por todas as verificações, adicionara os digitos a lista
        lista.append(numero)
    
    # Separadores de números e DDD
    lista.insert(2, '-')
    lista.insert(7, '-')

    print(20 * '=-')
    # Imprime a lista com todos os digitos lidos do usuário
    print(lista)

    print(20 * '=-')
    # Se o primeiro digito for 4 e o segundo for 1 (41) retorna 'True' para o usuário
    if lista[0] == 4 and lista[1] == 1:
        return True
    # Senão retornara 'False' para o usuário
    else:
        return False

# Imprime a função passado a lista de numero de telefone como parâmetro
print(verificar_ddd(numero_telefone))