caracteres_por_minuto = int(input('Quantos caracteres são digitados por minuto?'))  #Ler quantos caracteres são digitadas por minuto

caracteres_por_hora = caracteres_por_minuto * 60    #Para ver quantas caracteres são digitadas por hora, divide os caracteres por minutos por 60
paginas_por_hora = caracteres_por_hora/1000   #Para descobrir quantas páginas são digitadas por hora, divide as palavras por hora por 100, que é igual ao número de caracteres de uma página

print ('-=' * 12)      #Divisória

print (paginas_por_hora, 'páginas de 1000 caracteres digitadas por hora.')   #Ao final imprime o resultado de quantas páginas foram digitadas por hora

print ('-=' * 12)      #Divisória