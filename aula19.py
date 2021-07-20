#19 - Dicionários
#
#dados = {}
#dados = dict()
#dados = {'nome':'Pedro','idade':25 }
#print(dados['nome']  Pedro
#
#dados['sexo'] = 'M'  VAI ADICIONAR NA LISTA
#del dados['idade] DELETA
#
#
#print(filmes.values())  -> RETORNA TODOS OS VALORES DO DICIONARIO
#print(filmes.keys()) -> RETORNA AS CHAVES QUE DECLAOU Ex nome idade
#print(filmes.items()) -> RETORNA OS VALORES E AS CHAVES
#
#for key, values in filmes.items():
#   print(key, values)

#estado = dict()
#brasil = list()
#for c in range(0,3):
#   estado['uf'] = str(input('Unidade Federativa: '))
#   estado['sigla'] = str(input('Sigla': ))
#   brasil.append(estado.copy()) ### estado[:]
#for e in brasil:
#   for v in e.values(): # for k,v in e.items():
#       print(v)               print(k,v)
#
#90 programa lei nome e media de um aluno guardando a situaçao APROV ou rep se a media for 7 em um dicionario. no final mostre o conteudo
'''
alunos = dict()
alunos['nome'] = str(input('Nome do aluno: '))
alunos['media'] = float(input('Média do aluno: '))
if alunos['media'] >= 7:
    alunos['situacao'] = 'APROVADO'
elif  5 <= alunos['media'] < 7:
    alunos['situacao'] = 'RECUPERACAO'
else:
    alunos['situacao'] = 'REPROVADO'
print('=-'*15)
print(alunos)
for key, values in alunos.items():
    print(f' -{key} é igual a {values}')

#print(f'- nome aluno: {alunos["nome"]}')
#print(f'- média aluno: {alunos["media"]}')
#print(f'- aluno {alunos["situacao"]}')

#91 programa que 4 jogadores joguem um dado e tenha um resulado aleatorio. guarde esses valores em um dicionario, no final mostre o dicionario em ordem sabendo que o jogador que tirou o maior ganha
import random
import time
import operator
#jogo = dict()
#for c in range(0,4):
#    jogo['jogador' + str(c)] = random.randint(1,6)
#    print(jogo)

jogo = {'jogador1': random.randint(1,6),'jogador2': random.randint(1,6),'jogador3': random.randint(1,6),'jogador4': random.randint(1,6)}
rank = list()
for key, values in jogo.items():
    print(f'{key} tirou {values} no dado')
    time.sleep(1)
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print(rank)
for i,v in enumerate(rank):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')

#92 programa que leia nome, ano de nasc e carteira de trab. e cadastre-os com a idade em um dicionario se por acaso o CTPS  for diferente de zero, o dicionario recebera o ano de contratacao e o salario. calcule quantos anos a pessoa vai se aposentar.
import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.date.today().year)
print('#'*30)
for key, values in dados.items():
    print(f'- {key} tem o valor {values}')


#93 programa que leia o nome de um jogador de futb e quantar partidas ele jogou. depois ler a quantidade de gols feitos em cada partidada. no final guardar tudo em um dicionario inclusive o taotal de gols
jogador = dict()
gols = list()
soma = i = 0
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
while i < jogador['partidas']: # for c in range(0,jogador['partidas'])
    #soma = int(input(f'Quantos gols na partida {i}: '))
    #gols.append(soma)
    #soma += soma
    gols.append(int(input(f'Quantos gols na partida {i}: ')))
    i += 1
jogador['gols'] = gols[:]
#jogador['total'] = soma
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for key,values in jogador.items():
    print(f'O campo {key} tem o valor {values}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas ')
for i, v in enumerate(jogador['gols']):
    print(f'      => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')

#94 programa que leia o nome sexo idade de VArias pessoas guarde os dados em um dicionario e todos em uma lista. no final mostre quantas pessoas foram cadastradas, a media de idade do grupo uma lista com todas as mulheres, uma lista com todas as pesoas com as idades acima da media
dados = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: M/F: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F ')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    while True:
        opcao = str(input('Deseja continuar? S/N: ')).upper()[0]
        if opcao in 'SN':
            break
        print('Erro! DIgite apenas S ou N')
    if opcao == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(dados)} pessoas')
media = soma / len(dados)
print(f'A Media das pessoas cadastradas é {media:5.2f} anos')
print('As mulheres cadastradas foram: ', end=' ')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
    print()
print('As pessoas com idades acima da média: ')
for p in dados:
    if p['idade'] >= media:
        print(f'{p["nome"]}', end=' ')
    print()
print(dados)
'''
#95 aprimore o desafio  93 para que ele funcione com varios jogadores incluindo um sistema de vizualizacao de detalhes de aproveitamento  de cada jogador
jogador = dict()
time = list()
gols = list()
soma = i = 0
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    while i < jogador['partidas']:
        gols.append(int(input(f'Quantos gols na partida {i}: ')))
        i += 1
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        opcao = str(input('Deseja continuar? S/N')).upper()[0]
        if opcao in 'SN':
            break
        print('Erro, responda S ou N')
    if  opcao in 'S':
        i = 0
        jogador.clear()
        gols.clear()
    else:
        break
print('-='*30)
print(time)
print('-='*30)
print('cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
for key,values in enumerate(time):
    print(f'{key:>3} ', end='')
    for dado in values.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Qual joogador quer mostrar os detalhes? (999 para sair)'))
    if busca == 999:
        break
    if busca >= len(time):
        print('Jogador nao existe!')
    else:
        print(f'LEVANTAMENDO DO JOGADOR {time[busca]["nome"]}:')
        for i , g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i} fez {g} gols')
