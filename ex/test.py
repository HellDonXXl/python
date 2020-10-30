def media(lista):
    media = 0
    soma = 0

    for val in range(len(lista) ):
        soma = soma + lista[val]
        media = soma/len(lista)
        
    return media

n = int(input("Digite numero de linhas da lista: "))
listas = list(range(n))


for i in range(n):
    listas[i] = int(input("Digite um valor para [{}] : ".format(i)))


print(media(listas))