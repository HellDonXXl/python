''' 

programa triagulo.py
descrição: Lê os três lados do triagulo e informa ao usuario se ele é equilitero,isoceles ou escaleno
'''

import turtle

lado_a = float (input("escreva o valor do primeiro lado do triângulo: "))
lado_b = float(input("escreva o valor do segundo lado do triângulo: "))
lado_c = float(input("escreva o valor do terceiro lado do triâgulo: "))

#testar se é um triangulo
#para ser triangulo a soma dos lados menores deve ser maior que o lado maior

maior = 0.0

if(lado_a > lado_b and lado_a > lado_c):
    maior = lado_a
elif(lado_b > lado_a and lado_b > lado_c ):
    maior = lado_b
else:
    maior = lado_c

if(maior == lado_a):
    if(lado_b + lado_c < lado_a):
        print("as medidas passando como entrada não formam um triângulo")
        exit()
elif(maior == lado_b):
    if(lado_a + lado_c < lado_b):
        print("as medidas passando como entrada não formam um triângulo")
        exit()
else:
     if(lado_a + lado_b < lado_c):
        print("as medidas passando como entrada não formam um triângulo")
        exit()



#3 etapa: testar se é equilatero isocelo e escalo

if(lado_a == lado_b and lado_c == lado_b and lado_a == lado_c):
    print("é um equilatero")
   



elif (lado_a != lado_b and lado_c != lado_b and lado_a != lado_c):
    print("o triâgulo é isoceles")

else : print("o triâgulo é isóceles")
