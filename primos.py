numero = int(input("digite um numero: "))

primo = True

for i in range(2 , numero):
    if(numero%i == 0):
        primo = False
        print("Não é primo")
        break

if(primo == True):
    print("é primo")