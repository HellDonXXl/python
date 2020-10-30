print(
    '''
   1- [EX 1] Faça um Programa que peça dois números e imprima o maior deles
   2- [EX 2] Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
   3- [EX 3] Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido
   4- [EX 4] Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
   5- [EX 5] Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
      A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
      A mensagem "Reprovado", se a média for menor do que sete;
      A mensagem "Aprovado com Distinção", se a média for igual a dez.
   6- [EX 6]  Faça um Programa que leia três números e mostre o maior deles.
   7 - [Ex 7] Faça um Programa que leia três números e mostre o maior e o menor deles.
   8 - [EX 8] Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
   9  - [EX 9] Faça um Programa que leia três números e mostre-os em ordem decrescente.
   10 - [EX 10] Faça um Programa que pergunte em que turno você estuda. Peça para digitar:
   M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

     ''')
a = int(input("Digite o número da opção: "  ))

if(a == 1):
  
  n1= float(input("Digite um numero: "))
  n2 = float(input("Digite outro numero: "))

  if(n1 > n2):
      print("O numero {} é maior que {}".format(n1, n2) )

  elif (n2 > n1):
      print("O numero {} é maior que {}".format(n2, n1) )
  else:
      print("O numero {} é igual a {}".format(n1, n2) )

elif( a == 2): 
    n1 = float(input("Digite um numero: " ))
    if(n1 > 0):
        print("o número é positivo")
    elif(n1 < 0):
         print("O número é negativo" )
    else:
        print("O número é neutro")
elif(a == 3):
    sexo = input("Digite F - Feminino, M - Masculino: ")
    if(sexo ==  'F' or sexo == 'f'):
        print("você é do sexo feminino")
    elif(sexo == 'M' or sexo == 'm' ):
        print("você é do sexo Masculino")
    else:
         print("sexo invalido")   

elif(a == 4):
    
    letra = input("Digite uma letra: ")

    if( letra == "a" or letra =="e" or letra =="i" or letra == "o" ):
        print(" a letra é uma vogal")
    elif  letra.isdigit():
        print("você não digitou uma letra")
    else:
        print("a letra é consoante")

elif(a == 5):
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float (input("Digite sua segunda nota: ")) 
    media = (n1 + n2) / 2

    if(media == 10 ):
        print("Aprovado com Distinção")
    elif(media < 10 and media >= 7):
        print("Aprovado")
    else:
        print("Reprovado")    

elif(a == 6):
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    n3 = float(input("Digite outro numero: "))

    if(n1 > n2 and n1 > n3):
        print(f"o numero {n1} é maior que {n2} e {n3} ")
    elif(n2 > n1 and n2 > n3):
        print(f"o numero {n2} é maior que {n1} e {n3} ")
    elif(n3 > n1 and n3 > n2):
       print(f"o numero {n3} é maior que {n1} e {n1} ")
    else: 
        print("os numeros é igual")
elif(a == 7):
    n1 = float(input("Digite um numero: "))
    n2 = float(input("Digite outro numero: "))
    n3 = float(input("Digite outro numero: "))

    if(n1 > n2 and n1 > n3):
        if(n2 > n3):
         print(f"o numero {n1} é o maior numero e o {n3} é o menor numero " )
        else: 
            print(f"o numero {n1} é o maior numero e o {n2} é o menor numero " )
    elif(n2 > n1 and n2 > n3):
        if(n1 > n3):
         print(f"o numero {n2} é o maior numero e o {n3} é o menor numero " )
        else:
            print(f"o numero {n2} é o maior numero e o {n1} é o menor numero " )

    elif(n3 > n1 and n3 > n2):
        if(n1 > n2):
           print(f"o numero {n3} é o maior numero e o {n2} é o menor numero " )
        else:
            print(f"o numero {n3} é o maior numero e o {n1} é o menor numero " )
    else: 
        print("os numeros é igual")
elif(a == 8):
    n1 = float(input("Digite um numero:  "))
    n2 = float(input("Digite um numero:  "))
    n3 = float(input("Digite um numero:  "))

    if(n1 < n2 and n1 < n3):
        print(" o produto mais barato custa {:.2f}".format(n1))
    elif (n2 < n1 and n2 < n3):
        print(" o produto mais barato custa {:.2f}".format(n2))
    else:
        print(" o produto mais barato custa {:.2f}".format(n3))

elif(a == 9):
    n1 = float(input("Digite um numero:  "))
    n2 = float(input("Digite um numero:  "))
    n3 = float(input("Digite um numero:  "))

    if(n1 > n2 and n1 > n3):
        if(n2 > n3):
            print(f"a ordem é {n1} , {n2}, {n3} " )
        else: 
            print(f"a ordem é {n1}, {n3}, {n2} " )
    elif(n2 > n1 and n2 > n3):
        if(n1 > n3):
            print(f"a ordem é {n2}, {n1}, {n3} " )
        else:
            print(f"a ordem é {n2}, {n3}, {n1} " )

    elif(n3 > n1 and n3 > n2):
        if(n1 > n2):
           print(f"a ordem é {n3},  {n1},  {n2} " )
        else:
            print(f"a ordem é {n3}, {n2}, {n1} " )
    else: 
        print("os numeros é igual")

elif (a == 10):
 print("Qual turno você estuda: \n M - matutino \n V - Vespertino \n N- Noturno")
 B = input("Digite o período: ")
 if(B == "M" or B == "m" or B == "matutino" or B=="Matutino"):  
      print("Bom Dia!")
 elif (B == "V" or B == "v" or B == "Vespertino" or B == "verpertino"):
     print("Boa Tarde!") 
 elif (B == "N" or B == "n" or B == "Noturno" or B == "noturno"):
     print("Boa Noite!") 
 else:
     print("Você não estuda aqui")

elif(a == 11):
    print("Digite um numero de 0 a 10")
    n = int(input("Qual é o numero ? : "))

    while(n < 0 or n > 10):
        n = int(input("Qual é o numero ? : "))
elif(a == 12):
    nomeU = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")
    i = 0
    while nomeU == senha:
        print("Erro!. Senha errada")
        nomeU = input("Digite seu usuario: ")
        senha = input("Digite sua senha: ")
        
        i = int(i  + 1)

        print(i)

elif(a == 13):
   
    for i  in range(1,11):
      
        print( int(5*i))


 
  
