dia1 =int(input("Digite um dia: "))
mes1 = int(input("Digite um mes: "))
ano1 = int(input("DIgite um ano: "))

print("\n Escreve mais uma data a seguir \n")

dia2 =int(input("Digite um dia: "))
mes2 = int(input("Digite um mes: "))
ano2 = int(input("DIgite um ano: "))

#verificar que os dados são validos






if(ano1 > 0 and mes1 > 0 and dia1 > 0 and dia2 > 0 and ano2 > 0 and mes2 > 0):
 
  if(mes1 == 4 or mes1 == 6 or mes1 == 9 or mes1 == 11):
       #30 dias
       if(dia1 <= 30): 
           r = True
       else:
            r = False   
    

  elif(mes1 == 2):
        if(ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0 and dia1 <= 29 ):
            r = True
        elif(not(ano1 % 4 == 0 and ano1 % 100 != 0 or ano1 % 400 == 0) and dia1 <= 28):
            r = True   
        else: 
            r = False

  else:
        if(dia1 <= 31 and mes1 <=12):
            r = True
        else:
            r = False
        
     
   #verificação 2

  if(mes2 == 4 or mes2 == 6 or mes2 == 9 or mes2 == 11):
        if(dia1 <= 30): 
           r = True
        else:
            r = False   
    
  elif(mes2 == 2):
        if(ano2 % 4 == 0 and ano2 % 100 != 0 or ano2 % 400 == 0 and dia2 <= 29 and dia2 <= 29 ):
            r = True
        elif(not(ano2 % 4 == 0 and ano2 % 100 != 0 or ano2 % 400 == 0  ) and dia2 <= 28):
            r = True   
        else: 
            r = False
        
  else:
        if(dia2 <= 31 and mes2 <= 12):
            r = True
        else:
            r = False



  if (r == True ):
      if(ano1 > ano2):
           print("A data {} /{}/ {} é mais recente".format(dia1,mes1,ano1))
      elif(ano2 > ano1):
           print("A data {} /{}/ {} é mais recente".format(dia2,mes2,ano2))
           
      else:
          if(mes1 > mes2):
               print("A data {} /{}/ {} é mais recente".format(dia1,mes1,ano1))
          elif(mes2 > mes1):
               print("A data {} /{}/ {} é mais recente".format(dia2,mes2,ano2))
          else:
              if(dia1 > dia2):
                    print("A data {} /{}/ {} é mais recente".format(dia1,mes1,ano1))
              elif(dia2 > dia1):
                    print("A data {} /{}/ {} é mais recente".format(dia2,mes2,ano2))
              else: print("As datas são igual")
  else: print("Não é possivel verificar")
else:print("Não é possivel verificar")



