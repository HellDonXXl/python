ler = open("c:/Users/home/Desktop/PYTON/manipularStrig/valor.txt",'r')



media = 0
soma = 0
a = []
contador = 0
for linha in ler:
    contador = contador + 1
    a.append(float(linha))



print(a)

for i in range(len(a)):
    soma = soma + a[i]
    media = soma / contador
    print(media)



media = soma / contador

print("Media final: " ,media)
ler.close()