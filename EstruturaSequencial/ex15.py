salario_hora = float(input("Escreva o seu salario por hora: "))
horas_trabalhada = float(input("Escreva quantas horas você trabalhou: "))

salario = salario_hora * horas_trabalhada

porcetagem1 = 11 /100
porcetagem2 = 8/100
porcetagem3 = 5/100

imposto_renda = porcetagem1 * salario
inss =  porcetagem2 * salario
sidicato = porcetagem3 * salario

desconto = imposto_renda + inss + sidicato

salario_total = salario - desconto


print ("seu salario é: ", str(salario))
print ("imposto de renda é de : ", str(imposto_renda))
print ("o inss é de : ", str(inss))
print ("o sidicato : ", str(sidicato))
print("seu salario total é de: ", str(salario_total) )
