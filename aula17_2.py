#17 - Listas (Parte 2)
#LISTA DENTRO DE LISTA
#dados = ['Pedro',25]
#pessoas = []
#
#pessoas.append(dados[:])
#
#pessoas = [[Pedro,25],[Maria,19],[Joao,32]]
#print(pessoa[0][0]) = Pedro
#print(pessoa[1][1] = 19
#print(pessoa[1] = [Maria,19]

#galera = list()
#dados = list()
#for c in range(0,3):
#   dados.append(str(input('Nome: ')))
#   dados.append(int(input('Idade: ')))
#   galera.append(dados[:])
#   dados.clear()
'''
#84 programa que leia o nome e peso de varias pessoas guardando tudo em uma lista. no final mostre quantas pessoas foram cadastradas, uma listagem com as pessoas mais pesadas e leves
nomepeso = []
dados = []
maior = menor = 0
while True:
    nomepeso.append(str(input('Digite seu nome: ')))
    nomepeso.append(float(input('Digite seu peso: ')))
    if len(dados) == 0:
        maior = menor = nomepeso[1]
    else:
        if nomepeso[1] > maior:
            maior = nomepeso[1]
        if nomepeso[1] < menor:
            menor = nomepeso[1]
    dados.append(nomepeso[:])
    nomepeso.clear()
    opcao = str(input('Deseja continuar? S/N')).upper().strip()
    if opcao in 'N':
        break
print(dados)
print(f'O total cadastrado foi {len(dados)}')
print(maior,menor)
for p in dados:
    if p[1] == maior:
        print(p[0])
for p in dados:
    if p[1] == menor:
        print(p[0])

#85 programa onde usuario digite 7 valores numericos cadastre em uma lista mantenha separado os valores pares dos impares no final mostre-os em ordem crescente
num = [[],[]]
for posicao in range(0,7):
    n = (int(input('Digite um valor: ')))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os numeros PARES são {num[0]}')
print(f'Os numeors IMPARES são {num[1]}')

#86 programa que crie uma matriz de dimensao 3x3 preencha com valores listados no teclado no final mostre a matriz
matriz = [[],[],[]]
count = 0
for posicao in range(0,3):
    n = int(input(f'Digite o valor na posiçao [{count}],[{posicao}]'))
    matriz[0].append(n)
count += 1
for posicao in range(0,3):
    n = int(input(f'Digite o valor na posiçao [{count}],[{posicao}]'))
    matriz[1].append(n)
count += 1
for posicao in range(0,3):
    n = int(input(f'Digite o valor na posiçao [{count}],[{posicao}]'))
    matriz[2].append(n)
print(matriz[0])
print(matriz[1])
print(matriz[2])

#####OUTRA SOLUCAO
matriz = [[0,0,0],[0,0,0,],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posicao [{linha}],[{coluna}]'))
for linha in range(0,3): ## formatacao do print
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]',end='')
    print()

##### OUTRA SOLUCAO PARA A MINHA COM MENOS FOR
matriz = [[],[],[]]
for c in range(3):
    for l in range(3):
        matriz[c].append(int(input(f'Digite valor para [{c},{l}]: ')))
print(matriz)

#87 aprimore o ex anterior mostrando a soma de todos os valores pares a soma dos valores da terceira coluna o maior valor da segunda linha
matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = somac3 = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor na posiçao [{linha}],[{coluna}]'))
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]

for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]',end='')
    print()

print(f'A soma dos numeros PARES é: {somapar}')
######
##OUTRA SOLUCAO DO MAIOR
maior = 0
for coluna in range(0,3):
    if coluna == 0:
        maior = matriz[linha][coluna]
    elif matriz[linha][coluna] > maior:
        maior = matriz[linha][coluna]
######
print(f'O Maior valor da segunda linha é: {max(matriz[1])}')
#somac3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
for linha in range(0, 3):  # OUTRA FORMA DE SOMA A CORRETA
    somac3 += matriz[linha][2]
print(f'A Soma da terceira coluna é: {somac3}')

#88 programa que ajude um jogador da mega sena a criar palpites. programa vai perguntar quantos jogos sera gerado e vai sortear 6 numeros entre 1 a 60 para cada jogo cadastrar em uma lista composta
import random
listajogos = []
temp = []
cont  = 0
tot = 1
quant = int(input('Quantos jogos quer sortear? '))
while tot <= quant:
    while True:
        gerarnum = random.randint(1, 60)
        if gerarnum not in temp:
            temp.append(gerarnum)
            cont += 1
        if cont >= 6:
            temp.sort()
            cont = 0
            break
    listajogos.append(temp[:])
    temp.clear()
    tot += 1
#print(listajogos)
for i, l in enumerate(listajogos):
    print(f'Jogo {i+1}: {l}')
'''
#89 programa que leia o nome e 2 notas de varios alunos e guarde tudo em uma lista composta no final mostre um boletim contendo a media e permita que o usuario veja as notas individuais
dados = []
temp = []
while True:
    temp.append(str(input('Nome aluno: ')))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2:')))
    media = (temp[1]+temp[2]) /2
    temp.append(media)
    dados.append(temp[:])
    temp.clear()
    opcao = ' '
    opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opcao in 'N':
        break
print('-='*30)
print(f'{"No":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostre as notas de qual aluno? (999) para interromper'))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(dados) - 1:
        print(f'Notas de {dados[opc][0]} sao {dados[opc][1]} {dados[opc][2]}')
#print(dados)