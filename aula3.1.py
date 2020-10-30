
'''
Escreva um programa leia um ano e imprima ao
usuário se ele é bissexto ou não.

'''

ano = int(input(" insira um ano:  "))


if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0):
    print("o ano {} é Bissexto ".format(ano))

else:
    print("o ano {} não é Bissexto".format(ano))

