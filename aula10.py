#carro.siga()  carro é o OBJETO e siga METODO sempre com parentes
# if obj.met():
#   bloco_V_
# else:
#   bloco_F_
"""
tempo = int(input('Quantos anos tem seu carro: '))
if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')

##IF SIMPLIFICADO
print('Seu carro é novo' if <= 3 else 'Seu carro é velho')


#Programa que o computador pense em um numero inteiro entre 0 e 5 e peça para o usuario tentar decobrir qual foi o numero escolhido o programa deve escrever na tela se o usuario venceu
import random
import time
computador = random.randint(0,5) # metodo de intervalo de numero inteiro
print(computador)
print('Vou pensar em um numero de 0 a 5. Tente adivinhar')
jogador = int(input('Em que numero pensei: '))
print('PROCESSANDO')
time.sleep(2)
if jogador == computador:
    print('Parabens vc acertou!')
else:
    print('Errow!')

#Programa que leia a velocidade de um carro se ele ultrapassar 80km/h ele foi multado, e a multa custa 7 reais a cada km acima do limite
velocidade = float(input('Qual é a velocidade do carro? '))
if velocidade > 80:
    excedente = velocidade - 80
    valor = excedente * 7
    ## multa = (velocidade - 80) * 7
    print('Multa e pagara {}'.format(valor))
else:
    print('Sem multa')

#Programa que leia um numero qualquer na tela e mostre se ele é par ou impar
num = int(input('Digite um numero: '))
resto = num % 2
# (num % 2) == 0
if resto == 0:
    print('Seu numero é PAR')
else:
    print('Seu numero é IMPAR')

#programa que pergunte a viagens em KM calcule o preco da passagem cobrada 0,5 reais por km viagens de ate 200km 0,45 por km para as outras
km = float(input('Quantos km percorreu na viagem? '))
if km <= 200:
    print('Sua viagem sera de {}'.format(km * 0.5))
else:
    print('Sua viagem sera de {}'.format(km * 0.45))

#programa que leia um ano qualquer e mostre se ele é BISSEXTO
import datetime
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))

#programa que leia 3 numeros e mostre qual e o maior e o menor
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite um valor:'))
n3 = int(input('Digite um valor:'))
# Verifica o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#verifica o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O maior numero é {}'.format(maior))
print('O menor numero é {}'.format(menor))

#programa que leia o salario de funcionarios e calcule o valor de seu aumento para salarios superior a 1250 calcule um aumento de 10%   para inferiores ou igual o aumento de 15%
sal = float(input('Qual o salario do funcionario? R$:'))
if sal >= 1250:
    aumento = sal * (10/100)
    print('Seu novo salario sera de {}'.format(sal + aumento))
else:
    aumento = sal * (15/100)
    print('Seu novo salario sera de {}'.format(sal + aumento))

#programa que leia o comprimento de tres reta e diga ao usuario se pode ou nao formar um triangulo ex:
r1 = float(input('Digite um seguimento de reta:'))
r2 = float(input('Digite um seguimento de reta:'))
r3 = float(input('Digite um seguimento de reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos PODEM formar um triangulo')
else:
    print('Esses segmentos NAO PODEM formar um triangulo')
"""