
# abrir arquivo por leitura e escrita;

# escrever no arquivo v
'''
file = open("c:/Users/home/Desktop/PYTON/manipularStrig/abc.txt",'w+')
file.write('Linha 1 \n')
file.write('Linha 2 \n')
file.write('Linha 3 \n')

file.seek(0,0)
print('Lendo linhas: ')
print(file.read())

file.seek(0,0)
print("///////////////////")

print(file.readline(),end='')
print(file.readline(),end='')
print(file.readline(),end='')

print('//////////')
file.seek(0,0)
print(file.readlines())

file.close()
'''

'''
try:
    file = open("c:/Users/home/Desktop/PYTON/manipularStrig/abc.txt",'w+')
    file.write('linha')
    file.seek(0,0)
    print(file.read())

finally:
    file.close()
'''

'''
with open("c:/Users/home/Desktop/PYTON/manipularStrig/abc.txt",'w+') as file:
    file.write('Linha1\n')
    file.write('Linha2\n')
    file.write('Linha3\n')

    file.seek(0)
    
    print(file.read())
'''

import json

'''
d1 = {
    'Pessoa 1':
    {
        'nome':'Luiz',
        'Idade':25,
    },
    'Pessoa 2': 
    {
        'nome':'Rose',
        'Idade': 30,
    },


}

print(d1)

d2 = json.dumps(d1,indent=True)
print("////////////////")
print(d2)

with open("c:/Users/home/Desktop/PYTON/manipularStrig/abc.json",'w+') as file:
    file.write(d2)
    

'''
with open("c:/Users/home/Desktop/PYTON/manipularStrig/abc.json",'r') as file:
    d2 = file.read()
    d2 = json.loads(d2)
    print(d2)
    print(type(d2))

for k , v in d2.items():
    print(k)
    for k1, v1 in v.items():
        print(k1,v1)