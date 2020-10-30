'''  
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor 
'''


#123456
#1234 
#5/6

#popular// escola // é marcadas//  numeros de pessoas// exit() // 0 pedir; 

jose = 0
joao = 0
lucas = 0
matheus =0
nulo = 0
branco = 0




while True:
 

    print("bem vindo a voltação") 
 
    print('''vote:\n [1] José \n [2] João \n [3] Lucas \n [4] Matheus \n [5] Voto nulo \n [6] Voto em braco \n [0] acabo a votação ''')
    a = int(input("Digite seu voto: "))

    while (a < 0 or a > 6):
         a = int(input("Digite seu voto: "))
    
    if(a == 1):
        jose = jose +1
    elif(a == 2):
        joao = joao +1
    elif(a == 3):
        lucas = lucas +1
    elif(a == 4):
        matheus = matheus  + 1;          
    elif(a == 5):
        nulo = nulo + 1
    elif(a == 0):
        print(f"José:{jose}")
        print(f"João:{joao}")
        print(f"Lucas:{lucas}")
        print(f"Matheus:{matheus}")
        print(f"Nulo:{nulo}")
        print(f"Branco:{branco}")

        totalV = joao + jose + lucas + matheus + nulo + branco

        pNulo = ( nulo / totalV) * 100
        pBraco = (branco / totalV) * 100

        print("o porcentagem de nulo é {:.2f}%".format(pNulo))
        print("o porcentagem de Branco é {:.2f}%".format(pNulo))
        break

    else:
        branco = branco + 1
    


