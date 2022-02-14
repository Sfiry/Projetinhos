# A prefeitura de uma cidade desenvolveu um programa para cadastro dos moradores, e cada morador (não é especificada
# a quantidade) deve informar a sua idade. A prefeitura quer obter no final do cadastro a quantidade de moradores que
# são eleitores obrigatório, a quantidade de moradores que são eleitores facultativos e quantos moradores não são
# eleitores, de acordo com a tabela a seguir: Idade: Tipo de Eleitor >= 18 e <= 69           Obrigatório = 16 ou = 17
# ou >= 70   Facultativo < 16                    Não é eleitor Assim, faça um programa em Python que receba a idade
# de cada morador (quantidade indeterminada) e obtenha as quantidades requeridas pela prefeitura.

# Solução:

try:
    arquivo = open('dados.csv', 'r+')
except FileNotFoundError:
    arquivo = open('dados.csv', 'w+')
    n = 'ignorar'
    arquivo.write(n), arquivo.close()
qntpessoa = int(input('Quantas pessoas quer registrar?: '))
while 0 < qntpessoa:
    idade = int(input('Digite a Idade: '))
    if 15 < idade < 18 or idade > 69:
        print('O Voto é Facultativo')
    elif 17 < idade < 70:
        print('O Voto é Obrigatório')
    elif 16 > idade:
        print('Não Vota')
    escrevendo = '\r' + str(idade)
    file = open('dados.csv', 'r+')
    file_original = file.read()
    file.close()
    file = open('dados.csv', 'w+')
    file.write(file_original)
    file.write(escrevendo), file.close()
    qntpessoa = qntpessoa - 1
import csv

lista = []
facultativo = []
obrigatorio = []
eleitor = []
liste = []
with open('dados.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader)
    for linha in spamreader:
        lista.append(linha)
repeticoes = len(lista)
while repeticoes > 0:
    c = lista[0 - repeticoes]
    list_in_int = str((list(str(c)))[2:-2])
    list_in_int = list_in_int.replace("'", "").replace(',', '').replace(' ', '').replace('[', '').replace(']', '')
    numero = int(list_in_int)
    if numero == 16 or numero == 17 or numero > 69:
        facultativo.append(numero)
    elif 17 < numero < 70:
        obrigatorio.append(numero)
    elif numero < 16:
        eleitor.append(numero)
    repeticoes = repeticoes - 1
print('Neste municipio há', len(facultativo), 'pessoas cujo voto é facultativo')
print('Neste municipio há', len(obrigatorio), 'pessoas cujo voto é obrigatório')
print('Neste municipio há', len(eleitor), 'pessoas que não podem votar')
input('Aperte Enter para sair.')
