n = int(input("Digite um número"))

while(n<0):
 n = int(input("Digite um número"))

antant = 1
ant = 1

if (n==0 or n==1):
    print("o valor do enesimo termo é 1")

for i in range (2,n):
    termo = ant +antant
    antant = ant
    ant = termo
    
