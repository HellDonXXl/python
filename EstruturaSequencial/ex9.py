
print(''' converter\n [1] celsius para fahrenheit \n [2] fahrenheit para celsius\n [3 - sair]   ''')
opção = int(input("Qual opção você quer ?: "))

while (opção < 3):
    
    

    if opção == 1: 
     
     a = float(input("Digite o valor de celsius:"))

     f = (a * 1.8 ) + 32
     
     print("o valor de fahrenheit é {} ºF".format(f))
     
     e = int(input("você quer sair ? \n se sim digite 1 \n se não 0\n"))
     
     if(e == 1):
          exit()
     
    
    elif(opção == 2) :
     
     b = float(input("Digite o valor de fahrenheit:"))
     
     c = (b - 32) / 1.8

     print("o valor de celsius é {} ºC" .format(c))

     d = int(input("você quer sair ? \n se sim digite 1 \n se não 0\n   "))
     
     if(d == 1): 
         exit()



    else: 
        exit()
      





