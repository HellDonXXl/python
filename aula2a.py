#nome,idade,peso,sexo
#escreva 3 variáveis

Nome_Sexo = [input("Digite seu nome: ") , input("Seu sexo é Masculino ou Feminino:  ")    ]
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

 
print ("\n" + "Nome: ",Nome_Sexo[0] + "\n" + "Sexo:  ",Nome_Sexo[1] + "\n" + "Idade: " , str( idade) + "\n" + "Peso: " ,str( peso)  )
