'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''


nome = input("Digite seu nome:  ")

while len(nome) < 3:
   nome = input("Digite seu nome:  ")

idade = int(input("Digite sua idade: ")) 

while idade < 0 or idade > 150:
 idade = int(input("Digite sua idade: ")) 

Salario = float(input("Digite seu salario: "))

while Salario < 0:
 Salario = float(input("Digite seu salario: "))

sexo = input("Digite F que for feminino e M que for masculino: ")

while (sexo != "f" and sexo != "m" and sexo != "M" and sexo != "F") :
 sexo = input("Digite f que for feminino e n que for masculino: ")
 print(sexo)

estadoCivil = input("Digite seu Estado civil s - solteiro ; c - casado ; v - viuva ; d - divorciado")

while estadoCivil != "s" and estadoCivil != "c" and estadoCivil != "v" and estadoCivil != "d":
 estadoCivil = input("Digite seu Estado civil s - solteiro ; c - casado ; v - viuva ; d - divorciado")

print(f''' nome: {nome}
           idade: {idade}
           salario: {Salario}
           sexo: {sexo}
           Estado civil> {estadoCivil}
''')