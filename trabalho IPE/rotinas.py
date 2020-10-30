import os



def limpatela():
    os.system("cls")
    input("Aperte enter para continuar...")

def exibeMenu():
    print('''
-------------------------------------
|            trab_motors            |
-------------------------------------
| entre com a opção desejada:       |
| 1 - Cadastrar novo Carro          |
| 2 - Buscar por placa              |
| 3 - Excluir por placa             |
| 4 - Listar carros                 |
| 5 - Sair                          |
-------------------------------------''')

def novoCarro(listaCarros):
    ''' TO DO: documentar
    '''
    carro = {"nome":'',"marca":'',"placa":'',"km":0}
    
    for atrib in carro:
        if atrib == 'km':
            carro[atrib] = int(input("Digite quilometragem do veículo: "))

            while carro[atrib] < 0:
                carro[atrib] = int(input("Digite quilometragem do veículo: "))

            #TO DO: validar kilometragem
  


        elif atrib == 'placa':
               carro[atrib] = input("Digite a placa do veículo: ")
               b = False
               
               for i in range(len(listaCarros)):
                   if(carro[atrib] == listaCarros[i]['placa']):
                       b = True
                       break
                   else: 
                       b = False
                       break
                
                        
               while b == True:
                   carro[atrib] = input("Digite a placa do veículo: ")
                   for i in range(len(listaCarros)):
                       if(carro[atrib] == listaCarros[i]['placa']):
                           b = True
                           break
                       else: 
                            b = False
                            break


               while carro[atrib] == '' :
                    carro[atrib] = input("Digite a placa do veículo: ")
                

    
        else:
           carro[atrib] = input(f"Digite {atrib} do veículo: ")
           
            
           while carro[atrib] == '':
               carro[atrib] = input(f"Digite {atrib} do veículo: ")

          

    print(f"Veículo inserido com sucesso!")
    input() #para poder exibir a mensagem
    
    return carro

#TO DO: escrever as funções de busca, remoção e printagem de listas

def buscar(listaCarros):
    '''
    #TO DO: documentar
    '''
    print(listaCarros)
    print("\n Lista de veículos e a placa: \n")
    for i in  range(len(listaCarros)):
        print("Carro: {} | Placa: {} ".format(listaCarros[i]['nome'],listaCarros[i]['placa']))
    
    print()
     
    
    plac = input("Digite nome da placa que você está buscado: ")
    a = 0
    for i in range(len(listaCarros)):
        if(plac == listaCarros[i]['placa']):
              print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
              a = a+1
    if(a <= 0):
        print("Placa inexistente no cadastro")  

    print()    
              
        
    input()

    #pass #TO DO: implementar

def excluir(listaCarros):
    '''
    #TO DO: documentar
    '''
    print("\n Lista de veículos e a placa: \n")
    for i in  range(len(listaCarros)):
        print("Carro: {} | Placa: {} ".format(listaCarros[i]['nome'],listaCarros[i]['placa']))
    
    print()
  
    
    plac = input("Digite nome da placa que você quer excluir ou Enter para sair: ")
    
    if (plac != ""):
        a =-1
        b =-1
        for i in range(len(listaCarros)):
            if(plac == listaCarros[i]['placa']):
                print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
                a = a+2
                b = i
                break
        if(b > -1):
            del (listaCarros[b])
            print("removido ...")
            for i in range(len(listaCarros)):
                if(plac == listaCarros[i]['placa']):
                    print("Nome:{} || Marca: {} || Placa: {} || KM: {}".format(listaCarros[i]['nome'],listaCarros[i]['marca'],listaCarros[i]['placa'],listaCarros[i]['km']))
                    input()
            
            excluir(listaCarros)
           
        if(a <= 0):
            print("Placa inexistente no cadastro")    
          
    
    input()
    return listaCarros
    #pass#TO DO: implementar

def listar(listaCarros,numero):
    a = 0
    #Nome
    if(numero == 1):
        nome = input("Digite o nome do veículo: ")
        
        while nome == " ":
            nome = input("Digite o nome do veículo: ")
        
        
        for i in range(len(listaCarros)):
            if(nome == listaCarros[i]['nome']):
                a = a + 1
                
                
                print(f'''
Veículo {a}             
    Nome:  {listaCarros[i]['nome']}    
    Marca: {listaCarros[i]['marca']}   
    KM:    {listaCarros[i]['km']}      
    Placa: {listaCarros[i]['placa']}   ''')
                    
                                                    
        if(a <= 0):
            print("Nome inexistente no cadastro")
        


    #Marca
    elif(numero == 2):
        marca = input("Digite o Marca do veículo: ")
        
        while marca == " ":
            marca = input("Digite o Marca do veículo: ")
        
        
        for i in range(len(listaCarros)):
            if(marca == listaCarros[i]['marca']):
                a = a + 1
                
                
                print(f'''
Veículo {a}             
    Marca: {listaCarros[i]['marca']}   
    Nome:  {listaCarros[i]['nome']}    
    KM:    {listaCarros[i]['km']}      
    Placa: {listaCarros[i]['placa']}   ''')
                    
                                                    
        if(a <= 0):
            print("Marca inexistente no cadastro")

    #Quilomentragem
    elif(numero == 3):
        km = int(input("Digite o KM do veículo: "))
        
        while km < 0:
            km = int(input("Digite o KM do veículo: "))
        
        
        for i in range(len(listaCarros)):
            if(listaCarros[i]['km'] <= km):
                a = a + 1
                
                
                print(f'''
Veículo {a}             
    KM:    {listaCarros[i]['km']}      
    Marca: {listaCarros[i]['marca']}   
    Nome:  {listaCarros[i]['nome']}    
    Placa: {listaCarros[i]['placa']}   ''')
                    
                                                    
        if(a <= 0):
            print("KM inexistente no cadastro")        
     #Placa     
    elif(numero == 4):
        placa = input("Digite A Placa do veículo: ")
        
        while placa == " ":
            placa = input("Digite A Placa do veículo: ")
        
        
        for i in range(len(listaCarros)):
            if(placa == listaCarros[i]['placa']):
                a = a + 1
                
                
                print(f'''
Veículo {a}             
    Placa: {listaCarros[i]['placa']} 
    Marca: {listaCarros[i]['marca']}   
    Nome:  {listaCarros[i]['nome']}    
    KM:    {listaCarros[i]['km']}        ''')
                    
                                                    
        if(a <= 0):
            print("Placa inexistente no cadastro")

 
 
 

def exib (): 
  print('''
-------------------------------------
|            Listar carros          |
-------------------------------------
| entre com a opção desejada:       |
| 1 - Nome                          |
| 2 - Marca                         |
| 3 - Quilometragem                 |
| 4 - Placa                         |
-------------------------------------''')