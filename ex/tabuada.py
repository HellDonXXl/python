def tabuada(a):
    resutado = 0
    lista = []
    for i in range(10):
        resutado = a * (i + 1)
        lista.append(resutado)

    return lista


b = int(input("Digite um número para receber a sua tabuada: "))
 
tabu = tabuada(b)

for i in range(10):
   print("{} x {} = {} " . format(b,i+1,tabu[i]))   
