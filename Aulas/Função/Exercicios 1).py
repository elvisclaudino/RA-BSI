def intervalo(n1, n2, n):
    if n >= n1 and n <= n2:
        return True

    return False

inicio = int(input("Qual o primeiro numero do intervalo: "))
fim = int(input("Qual o primeiro numero do intervalo: "))
valor = int(input('Qual o numero que deseja testar se está dentro do intervalo: '))

resultado = intervalo(inicio, fim, valor)
print(resultado)