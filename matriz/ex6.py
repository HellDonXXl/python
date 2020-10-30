matriz = list(range(4))
for i in range(0,4):
    matriz[i]=list(range(4))
for i in range(0,4):
    for j in range(0,4):
        matriz[i][j] = int(input("Digite um valor para [{},{}] : ".format(i,j)))
print()
a = 1
for i in range (0,4):
    for j in range(0,4):
      
      
       if(matriz[i][j] != matriz[j][i]):
           a = 0
                   
for i in range(4):
  for j in range(4):
    print('[{}]'.format(matriz[i][j]),end = '')
  print()    
print()
if(a == 0):
    print("A matriz é uma matriz assimétrica ")
else:
    print("A matriz é  uma matriz simétrica ")
