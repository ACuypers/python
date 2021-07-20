#014 - Estrutura de repetição while
# c = 1
# while c < 10:
#    print(c)
#    c = c + 1
#print('FIM')
#GERALMENTE WHILE VC NAO SABE O FIM

#programa que leia o sexo de uma pessoa mas so aceite M e F. caso esteja errado peça para digitar novamente valor correto
'''
#c = 1
#while c == 1:
#    sexo = str(input('Qual o seu sexo M ou F? ')).upper().strip()[0]
#    if sexo in 'M' or sexo in 'F':
#        c = 0
#    else:
#        print('Tente novamente')
#print('Sexo {} registrado'.format(sexo))

sexo = str(input('Qual o seu sexo M ou F? ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados errados, informe novamente: ')).upper().strip()[0]
print('Sexo {} registrado'.format(sexo))


#melhor o jogo do desafio 28 onde o pc pensa em um numero de 0 a 10 so que o jogador vai tentar adivinhar ate o acertar mostranqdo quantos palpites foram dados para vencer
#import random
#computador = random.randint(0,10)
#print(computador)
#jogador = int(input('Digite um numero entre 0 e 10: '))
#count = 1
#while jogador != computador:
#    jogador = int(input('Ainda nao é o numero correto tente novamente: '))
#    count += 1
#print('Parabens vc acertou na {} tentativa'.format(count))

import random
computador = random.randint(0,10)
print(computador)
acertou = False
count = 0
while not acertou:
    jogador = int(input('Digite um numero entre 0 e 10: '))
    count += 1
    if jogador > computador:
        print('O valor pensado é MENOR')
    elif jogador < computador:
        print('O valor pensado é MAIOR')
    else:
        acertou = True
print('Parabens vc acertou na {} tentativa'.format(count))


#programa que leia 2 valores  mostre o menu na tela [1] soma [2] multiplicacao [3] maior [4] novos numeros [5]sair do programa, deve realizar a operacao solicitada
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor:'))
opcao = 0
while opcao != 5:

    print(' [1] soma \n [2] multiplicacao \n [3] maior \n [4] novos numeros \n [5] sair do programa')
    opcao = int(input('Qual sua opção? '))
    print('=-='*10)
    if opcao == 1:
        soma = n1 + n2
        print('O resultado {} + {} = {}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado {} x {} = {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            print('O maior numeor é {}'.format(n1))
        else:
            print('O maior numero é {}'.format(n2))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor NOVAMENTE: '))
        n2 = int(input('Digite o segundo valor NOVAMENTE:'))
    elif opcao == 5:
        sair = True
    else:
        print('Opcao invalida')
    print('=-='*10)

#programa que leia um numero qualquer e mostre seu fatorial ex: 5! 5*4*3*2*1
#import math
#n = int(input('Calcule seu Fatoria:'))
#f = math.factorial(n)
#print('O Fatorial de {} é {}'.format(n,f))

n = int(input('Calcule seu Fatorial: '))
c = n
f = 1
while c > 0:
    print('{}  '.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))

#refaça o desafio 61 lendo o primeiro termo de uma PA e a razao mostre os 10 primeiros numeros
termo1 = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razao da PA: '))
termo = termo1
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end=' ')
    termo += razao
    cont += 1
print('FIM')

#melhore o desafio 61 perguntando para o usuario se ele que mostrar mais algum termo.programa para qunaod ele digitar 0
termo1 = int(input('Qual o primeiro termo da PA: '))
razao = int(input('Qual a razao da PA: '))
termo = termo1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('FIM')

#escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementeos de uma sequancia de fibonaci ex: 0 -1 -1 -2- 3- 5 -8
print('-'*25)
print('Sequancia de Fibonacci')
print('-'*25)
n = int(input('Quantos termos quer mostrar? '))
ants = 0
dps = 1
print('0 - 1 - ',end='')
while n != 2:
    termo = ants + dps
    ants = dps
    dps = termo
    print('{} -' .format(termo),end=' ')
    n -= 1
print('FIM')

#programa que leia varios numeros inteiros. programa so vai parar quanado o usuario digitar 999. no final mostre quantos numeros foram digirtados e qual foi a soma entre eles desconsiderando o 999
digito = 0
count = 0
soma = 0
digito = int(input('Digite um numero: '))
while digito != 999:
    soma = soma + digito
    count += 1
    digito = int(input('Digite um numero: '))
print('Foram digitados {} e a soma entre eles é {}'.format(count,soma))

#programa que leia varios numeros inteiros, no final mostre as medias entre todos o maior e o menor valor o programa deve pergguntar ao usuario se ele quer ou nao continuar
digito = 0
div = 0
soma = 0
media = 0
maior = 0
menor = 0
continuar = False

while not continuar:
    digito = int(input('Digite um numero: '))
    div += 1
    soma = soma + digito
    media = soma / div
    continuar = str(input('Deseja continuar S / N: ')).upper()
    if continuar == 'S':
        continuar = False
    else:
        continuar = True
    if div == 0:
        menor = maior = digito
    else:
        if digito > maior:
            maior = digito
        else:
            menor = digito

print('Voce digitou {} numeros e a media deles é {}'.format(div,media))
print('O Maior valor é {} e o Menor {}'.format(maior,menor))

'''