nomeU = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
i = 0
while nomeU == senha:
 print("Erro!. Senha errada")
 nomeU = input("Digite seu usuario: ")
 senha = input("Digite sua senha: ")
        
 i = int(i  + 1)

 print(i)