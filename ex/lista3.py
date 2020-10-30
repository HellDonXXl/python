def listaL (listas):
    a = listas.copy()
    a.reverse()
    b = listas.copy()
    b.sort()
    junto = [listas,a,b]
    return junto
n = int(input("Digite o tamanho da sua lista: "))
lista =list(range(n)) 
for i in range(n):
    lista[i] = int(input("Digite um valor para [{}]: ".format(i)))
junto = listaL(lista)
print(junto)


