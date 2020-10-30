tm_arquivo = float(input('Informe o tamanho do arquivo para donwload (em MB): '))
vl = float( input('Informe a velocidade de sua internet (em MBPS): '))

tempo = tm_arquivo / vl
minuto = tempo / 60.0

print ('O tempo aproximado para download do arquivo usando este link e de: {:.2f} minutos'.format(minuto))