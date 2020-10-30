metros = float(input("Qual é tamanho em metros quadrados da área a ser pintada "))

litro = metros / 6 
b = litro / 3.6
d = int(b)
if(b == d):
        c = int(b) * 25
        
        print("{}  || {}".format(b,c))
else:
     f = int(b) + 1
     g = f * 25
     print( "{}   ||  {}".format(f,g))

    