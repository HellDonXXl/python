from time import sleep
def exibir_menu():
    print('''\n\033[1m\033[33mEscolha uma opção:\033[0;0m
   
    [1] Cadastrar um veículo
    [2] Listar veículos cadastrados
    [3] Procurar dados de um veículo
    [4] Remover veículo cadastrado
    [5] Finalizar programa
    ''')
veiculo = 0
veiculos = []
def cadastrar(veiculos):
    marca = input('Marca? ')
    nome = input('Nome? ')
    placa = input('Placa? ')
    quilometragem = leiaInt('Quilometragem? ')
    veiculos.append((marca, nome, placa, quilometragem))

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        quilometragem = str(input(msg))
        if quilometragem.isnumeric():
            valor = int(quilometragem)
            ok = True
        else:
            print('\033[0;31mDigite um número inteiro válido!\033[m')
        if ok:
            break
    return valor

def listar(veiculos):
    for veiculo in veiculos:
        marca, nome, placa, quilometragem = veiculo
        print(f'Nome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}')

def buscar(veiculos):
    b = 0
    marca_desejada = input('Marca? ')
    for veiculo in veiculos:
        marca, nome, placa, quilometragem = veiculo
        if marca == marca_desejada:
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
          b = b +1
          
    if(b == 0):
        print(f'\033[0;31mVeículo com marca {marca_desejada} não encontrada\033[m')
     
    nome_desejado = input('Nome? ')
    b = 0
    for veiculo in veiculos:
        marca, nome, placa, quilometragem = veiculo
        if nome == nome_desejado:
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
          b = b + 1
    if(b == 0):
        print(f'\033[0;31mVeículo com nome {nome_desejado} não encontrado\033[m')
           
            
    quilometragem_desejada = int(input('Quilometragem? '))
    b = 0
    for veiculo in veiculos:
      marca, nome, placa, quilometragem = veiculo
      if quilometragem <= quilometragem_desejada:
        print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
        b = b + 1
    if(b == 0):
        print(f'\033[0;31mVeículo com nome {nome_desejado} não encontrado\033[m')
    placa_desejada = input('Placa? ')
    b = 0
    for veiculo in veiculos:
        marca, nome, placa, quilometragem = veiculo
        if placa == placa_desejada: 
          print(f'\033[32mNome: {nome}, Quilometragem: {quilometragem}, Marca: {marca}, Placa: {placa}\033[0;0m')
          b = b + 1
    if(b == 0):
        print(f'\033[0;31mVeículo com nome {nome_desejado} não encontrado\033[m')

def Delete(veiculos):
  veiculo_desejado = input('Digite a placa do veículo que deseja excluir:\n')

  b = -1
  if(veiculo_desejado != " "):
      
      for i in range(len(veiculos)):
          if(veiculo_desejado ==  veiculos[i][2]):
              b = i
              break
              
  if(b >= 0):
      print('Removido ',veiculos[b])
      del(veiculos[b])
      print(veiculos)
  else:
      print('Placa não existe')
      
def main():
    veiculos = []

    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(veiculos)
            sleep(1)
        elif opcao == 2:
            listar(veiculos)
            sleep(1)
        elif opcao == 3:
            buscar(veiculos)
            sleep(1)
        elif opcao == 4:
            Delete(veiculos)
            sleep(1)
        elif opcao == 5:
            print('\n\033[0;31mPrograma Finalizado!\033[m\n\n\n') 
            sleep(1)
            exit()
        else:
            print('\033[0;31mDigite uma opção válida!\033[m')
            sleep(1)
main()