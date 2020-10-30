
print("1 - Homem\n 2- Mulher")
opcao = int(input("Você é oque ?: "))

if(opcao == 1):
 a = float(input("Digite sua altura: "))
 p = (72.7 * a) - 58 
 print("seu peso ideal é {}".format(p))
elif(opcao == 2):
    b = float(input("Digite sua altura: "))
    m = (62.1 * b) - 44.7
    print("seu peso ideal é {}".format(m))
else: print("você não é humano, como entro no pc animal")