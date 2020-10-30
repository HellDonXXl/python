def fatorial(numero):
    # o fatorial de 0 ou 1 = 1
    if (numero == 0 or numero == 1):
        return 1
    # a função vai chama ela mesma quantas vez for nescessaria,
    # para pega o valor de um fatorial ex 6! - 1! = 5! - 1 = 4! ... 
    # Assim vai fazendo numero * seu antecessor até chega no 1;
    else:
        return numero * fatorial(numero - 1)


n = int(input("Digite um numero: "))
res = fatorial(n)

print("O fatorial de {} é {}" .format (n,res))