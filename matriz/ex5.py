valores = ['A' , '2' , '3', '4', '5', '6','7','Q','J','K']
nipes = ['Copas', 'Paus' , 'espada', 'ouros']
cartas = []

for valor in valores:
    for nipe in nipes:
        carta = valor + ' de ' + nipe
        cartas.append(carta)

print(cartas)