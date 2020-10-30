metros = float(input("Qual é tamanho em metros quadrados da área a ser pintada "))

if(metros >86,4):
  litro = metros / 6 
  qt_latas = litro / 3.6
  d = int(qt_latas)
  if(qt_latas == d):
        

        resto = qt_latas % 5
        qt_galao = int(qt_latas /5)
        resto = qt_galao * 5
        t = qt_latas - resto

        total = (qt_galao * 80) + (t*25)
        print (" você precisa de {} latas  e {} galão e o valor é R${:.2f}",t,qt_galao)
        
            
  else:
     f = int(qt_latas) + 1
     qt_galao = int(f /5)
     w = qt_galao * 5
     t = f - w

     total =(t * 25) + (qt_galao * 80) 
     print( "você precisa de {} latas  e {} galão o valor  é R${:.2f}".format(t,qt_galao,total ))
   

else :
   metros = float(input("Qual é tamanho em metros quadrados da área a ser pintada "))
   litro = metros / 6 
   qt_latas = litro / 3.6
   d = int(qt_latas)
   if(qt_latas == d):
      total = int(qt_latas) * 25
        
      print("você precisa de {} latas  o valor é R${:.2f}".format(qt_latas,total))
   else:
      f = int(qt_latas) + 1
      total = f * 25
      print( "você precisa de {} latas  o valor é R${:.2f} ".format(f,total))
