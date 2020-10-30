'''Escreva um programa que pegue uma lista de 10 elementos numéricos e
imprima o valor da soma e a média desses valores sem usar a função sum()
'''

vet = list(range(10))

for i in range(10):
    vet[i] = int(input("Digite 10 valores : "))

soma = 0

for i in range(10):
    soma = soma + vet[i]

print(vet)
print(soma)
media = soma / 10

print(media)

