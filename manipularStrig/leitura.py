ler = open("c:/Users/home/Desktop/PYTON/manipularStrig/poema.txt",'r')
esc = open("c:/Users/home/Desktop/PYTON/manipularStrig/caracter.txt",'w')


a = []

#print(ler.read())

#print(ler.readline())
#print(ler.readline())

#print(ler.readlines())

for linha in ler:
    linha = linha.rstrip()
    print(linha)
    a.append(linha)

ler.close()
esc.close()

print(a)
print(a[0])