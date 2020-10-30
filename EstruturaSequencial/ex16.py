metros = float(input("Qual é tamanho em metros quadrados da área a ser pintada "))

litro = metros / 3
b = litro / 18
d = int(b)
if(b == d):
        c = int(b) * 80
        
        print(" você precisa de {} latas e o valor delas é  R${:.2f}".format(b,c))
elif (d <= 0):
        print("não tem tamanho para pintar")
else: 
        f = int(b) + 1
        g = f * 80
        print( "você precisa de {} latas e o valor delas é R${:.2f}".format(f,g))