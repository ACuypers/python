#Estrutura de repetição for
#for c in range(1,10):

#for c in range(1,6):
#    print(c)
#print('FIM')

#for c in range(6,0, -1):
#    print(c)
#print('FIM')

#for c in range (0,7,2):
#    print(c)
#n = int(input('Digire um numero: '))
#for c in range (0, n):
#    print(c)

#i = int(input('Inicio'))
#f = int(input('FIM'))
#p = int(input('PASSO'))

#for c in range(i, f+1, p):
#    print(c)

#s = 0
#for c in range(0, 4):
#    n = int(input('Digite um valor: '))
#    s = s + n # s += n
#print('O somatorio de todos os valores foi {}'.format(s))
'''
#Programa que faça a contagem regressiva para o esoturo de fogos de artificio indo de 10 até 0 com pausa de 1 segundo entre eles
import time
for cont in range(10,0-1,-1):
    print('Contagem regressiva {}'.format(cont))
    time.sleep(1)
print('BUM!!!')

#Programa que mostre todos os numeros PARES que estao no intervalo de 1 a 50
for c in range(1,50+1,2):
    print(c+1, end=' ')
print('\n')
for c in range(0,50+1,2):
    print(c,end=' ')
print('\n')
for n in range(1,51):
    if n % 2 == 0:
        print(n,end=' ')
print('\n')
for n in range(2,51,2):
    print(n,end=' ')
#Programa que calcule a soma entre todos os numeros IMPARES que soa multiplos de tres e que se encontram no intervlo de 1 ate 500
soma = 0
for c in range(1,500+1): # (1,501,2)
    if c % 2 != 0 and c % 3 == 0: # c % == 0:
        soma += c
        print(c, end=" ")
print('\n {}' .format(soma))
#Refaca o desafio 9 mostrando a tabuada que o usuario escolher porem com laco for
tabuada = int(input('Qual tabuada deseja saber? '))
for c in range(1,10+1):
    resultado = c * tabuada
    print('{} x {} = {}'.format(tabuada,c,resultado))

#Programa que leia seis numeros interios e mostre a soma apenas nos PARES se for impar desconsiderar
soma = 0
for c in range(1,6+1):
    n = int(input('Digite o {} numero: '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos numeros PARES que escolheu é {}'.format(soma))

#Programa que leia o primeiro termo e a razao de uma PA no final mostre os 10 primeiros termos
termo1 = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razao da PA: '))
for c in range(termo1,termo1+(10*razao),razao): #decimo = primeiro + (10-1) + razao e no range colocou decimo + razao
    print(c, end=' ')

#Programa que leia um numero inteiro e diga se eh ou nao primo : numeros primos sao divisiveis por 1 ou ele mesmo
np = int(input('Digite um numero para saber se é primo: '))
tot = 0
for c in range(1, np+1):
    if np % c == 0:
        print('\033[33m', end=''))
        tot += 1
    else:
        print('\033[33m', end=''))
    print ('{}'.format(c), end=''
print('o numero  {}  foi divisivil {} vezes'.format(np,tot)
if tot == 2:
    print('Por isso é PRIMO')
else:
    print('NAO E PRIMO')

#programa que leia uma frase qualquer e diga se ela é um PALINDROMO desconsiderando os espacos ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA
frase = str(input('Digite uma frase')).strip().upper()
palavras = frase.split()
junto = ''.join.palavras()
inverso = ''
for letra in range (len(junto) -1 ,0 -1 ,-1):
    inverso += junto[letra]
if inverso == junto
    print('temos um palindromo):
else:
    print('NAO eh')
#Programa que leia o ano de nascimento de 7 pessoas. no final mostre quantas pessoas nao atingiu a maioridade(21) e quantas sao maiores
import datetime
menores = 0
maiores = 0
for c in range(1,7+1):
    ano = int(input('{} Qual seu ano de nascimento?'.format(c)))
    if datetime.date.today().year - ano < 21:
        menores += 1
    else:
        maiores += 1
print('Nao atingiu a maioridade {} e sao de maiores {}'.format(menores,maiores))

#Programa que leia o peso de cinco pessoas no final mostre qual foi o maior e o menor peso
maior = 0
menor = 0
#lista = []
for c in range(1,5+1):
    peso = float(input('{} Qual seu peso?'.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}'.format(maior))
print('O menor peso é {}'.format(menor))
##    lista.append(peso)
##print(lista)

#Programa que leia nome idade sexo de 4 pessoas no final a media de idade qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
soma = 0
media = 0
maioridadeh = 0
nomevelho = ''
count = 0
for p in range(1,5):
    print('----- {} Pessoa -----' .format(p))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo M ou F: '))
    soma += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        count += 1
print('O homem mais velho é {} com idade de {}'.format(nomevelho,maioridadeh))
media = soma / 4
print('A média do grupo é de {}'.format(media))
print('Exite {} mulheres com menos de 20 anos'.format(count))
'''
