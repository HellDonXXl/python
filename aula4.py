
soma = 0 
media = 0
menor = 0
maior = 0

vezes  = int(input("Digite um valor: "))

for i  in range (vezes):
 
  valor = float(input("Digite um valor "))
  soma = soma + valor

  if(i == 0):
      menor = valor

  if(valor > maior):
     maior = valor
  elif(valor < menor):
      menor = valor

media = soma / vezes   
print(f''' some: {soma} 
           maior: {maior}
           menor valor: {menor}
           media = {media}''')

