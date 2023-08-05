# Função que analisa se o número de alunos na classe é PAR ou IMPAR
def numero_par_ou_impar_de_alunos():
    # Lê do teclado quantos alunos há na turma
    valor = int(input('Quantos alunos há na turma? '))

    # Se o valor for positivo, realizara a conta de resto de divisão inteira
    if valor >= 0:
        print(20 * '=-')
        x = valor % 2
        
        # Se o resto for igual a 0, retornara 'True' ao usuário
        if x == 0:
            return True
        # Senão retornara 'False' ao usuário
        else:
            return False
    
    # Senão retornara 'Valor negativo' ao usuário
    else:
        print(20 * '=-')
        return('Valor negativo') 

# Imprime o retorno da função
print(numero_par_ou_impar_de_alunos())