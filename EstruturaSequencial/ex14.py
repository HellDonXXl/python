peso = int(input("Qual peso do peixes que você pego? "))

if(peso > 50): 
    ex_peixe = peso - 50
    muta = ex_peixe * 4.00

    print("Você tem {} quilos de peixe \n o maximo é 50 quilos e você tem {} a mais \n sua muta é de  R${:.2f} " .format(peso,ex_peixe,muta))

else : print("você tem {} e não tem muta" . format(peso))