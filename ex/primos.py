
def ehPrimo (x):
    
    if(x == 2):
        return True
        
    for i in range(2,x+1):
        
        if(x%i == 0):
            return False
            break
        else:
            return True
    






b = int(input("Digite um numero: "))
while(b < 1):
    b = int(input("Digite um numero inteiro: "))


print(ehPrimo(b))


