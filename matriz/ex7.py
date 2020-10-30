lista = list()
chavez = dict()
numeroV = int(input('Digite numero de carros você quer: '))
for c in range(0,numeroV):
    chavez['Carro'] = str(input("Digite o modelo do carro: ")) 
    chavez['Placa'] = str(input("Digite a placa do carro: "))
    chavez['Quilometragem'] = int(input("Digite a quilometragem do carro: "))
    lista.append(chavez.copy())
maiorQ = 0
oID = -1
for c in range(0,numeroV):
   
   if(lista[c]['Quilometragem'] > maiorQ):
       maiorQ = lista[c]['Quilometragem']
       oID = c
    
print()
print('O Carro com amior Quilometragem é {} com placa {} e sua quilometrage foi de {}'.format(lista[oID]['Carro'],lista[oID]['Placa'],lista[oID]['Quilometragem']))
a = input("Digite uma placa que você busca: ")
for i in range(numeroV):
    if (a == lista[i]['Placa']):
        print('O Carro é {} com placa {} e sua quilometrage foi de {}'.format(lista[i]['Carro'],lista[i]['Placa'],lista[i]['Quilometragem']))
        break
    
        
       