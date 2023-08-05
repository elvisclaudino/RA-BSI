nota = float(input('Qual a nota de 0 à 100?'))      #Ler a nota aplicada pelo professor

print ('-=' * 12)   #divisória

while nota < 0 or nota > 100:   #enquanto a nota não estiver entre 0 e 100
    print ('Digite um valor válido entre 0 e 100')  #aviso para digitar um valor valido
    nota = float(input('Qual a nota de 0 à 100?'))  #ler novamente o valor

if nota == 0:    #se a nota for igual a zero
    print ('O aluno recebeu conceito E')    #imprime o conceito equivalente a nota que o aluno recebeu
elif nota >= 1 and nota <= 35:   #se a nota estiver entre 1 e 35
    print ('O aluno recebeu conceito D')    #imprime o conceito equivalente a nota que o aluno recebeu
elif nota >= 36 and nota <= 60:  #se a nota estiver entre 36 e 60
    print ('O aluno recebeu conceito C')    #imprime o conceito equivalente a nota que o aluno recebeu
elif nota >= 61 and nota <= 85:  #se a nota estiver entre 61 e 85
    print ('O aluno recebeu o conceito B')  #imprime o conceito equivalente a nota que o aluno recebeu
else:   #caso o aluno tire acima de 86
    print ('O aluno recebeu conceito A')    #imprime o conceito equivalente a nota que o aluno recebeu

print ('-=' * 12)   #divisória