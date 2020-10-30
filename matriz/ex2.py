n = int(input("Digite numero de linhas: "))
m = int(input("Digite numero de colunas: "))
mat = list(range(n))
for i in range(0,n):
  mat[i] = list(range(m))
for i in range(n):
  for j in range(m):
    mat[i][j] = int(input("Digite um valor para [{},{}]: ".format(i,j)))
print('///'*30)
for i in range(n):
  for j in range(m):
    print('[{}]'.format(mat[i][j]),end = '')
  print()    
maior = 0
menor = mat[0][0]
soma = 0
vez = n * m
for l in range(n):
  for k in range(m):
    if(mat[l][k] > maior):
      maior = mat[l][k]
    if(mat[l][k] < menor):
      menor = mat[l][k]
    soma =soma + mat[l][k]
media = soma / vez
print()
print("O maior numero é:{}".format(maior))
print()
print('O menor numero é: {}'.format(menor))
print()
print('A soma é {}' .format(soma))
print()
print('A media é {:.2f}'.format(media))
for l in range(n):
  for k in range(m):
    if(l == 0 and k == 0):
        print("Os elemento maior que 10 são: \n")
    if(mat[l][k] > 10):
      print("[{}]".format(mat[l][k]))

      