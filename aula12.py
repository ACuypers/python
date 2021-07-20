#Condições Aninhadas
#if elif else

#Programa para aprovar um emprestimo de uma casa. Vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.Calcule o valor da prestacao mensal sabendo que ela nao pede exceder 30% do salario ou entao o emprestimo sera negado
'''
casa = float(input('Qual o valor da casa: R$'))
salario= float(input('Qual seu salario: R$'))
anos = int(input('Quantos anos irá pagar: '))

prestacao = casa / (anos * 12)
exceder = salario * (30/100)
print(prestacao , exceder)
if prestacao > exceder:
    print('Negado')
else:
    print('Aprovado')

#Prgorama que leia um numero inteiro qualquer e peça para o usuario escolher a base de conversao 1 para binario 2 octal 3 hexadecimal
num = int(input('Digite um numero interio:'))
print('Escolha uma das bases para conversão: \n [ 1 ] converter para BINARIO\n [ 2 ] converter para OCTAL \n [ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção:'))
if opcao == 1:
    print('O numero ficou {}'.format(bin(num)))
elif opcao == 2:
    print('O numero ficou {}'.format(oct(num)))
elif opcao == 3:
    print('O numero ficou {}'.format(hex(num)))
else:
    print('Opcao invalida tente novmante')

#Programa que leia 2 numeros inteiros e compare-os mostrando primeiro valor e maior, o segundo valor e maior os dois sao iguais
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

if n1 > n2:
    print('O MAIOR numero é {} e o menor numero é {}'.format(n1 , n2))
elif n1 < n2:
    print('O MAIOR numero é {} e o menor numero é {}'.format(n2 , n1))
else:
    print('Os numeros são IGUAIS {}'.format(n1))

#Programa que leia o ano de nascimento de um jovem e informe com sua idade se ele ainda vai se alistar ao servico militar, se é hora de se alistar, se ja passou do tempo e o programa mostra o tempo que falta ou passou
import datetime
ano = int(input('Qual seu ano de nascimento? '))
anoatual = datetime.date.today().year

if anoatual - ano == 18:
    print('Este ano é o seu ALISTAMENTO militar')
elif anoatual - ano > 18:
    passou = (anoatual - ano) - 18
    print('Ja passou {} anos para o seu alistamento'.format(passou))
else:
    falta = 18 - (anoatual - ano)
    print('Ainda falta {} anos para o seu alistamento'.format(falta))

#Programa que le a duas notas do aluno faca a media e mostre a msg, abaixo de 5 reprovado 5 a 6.9 recuperacao e 7 aprovado
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print('Aprovado e sua média foi {}'.format(media))
elif 7 > media >= 5: # media >= 5 and media < 7
    print('Ficou de RECUPERACAO e sua media foi {}'.format(media))
else:
    print('Reprovado e sua media foi {}'.format(media))

#Programa que leia o ano de nascimento de atletas e mostre sua categoria ate 9 anos mirim ate 14 anos infaltil 19 junior 20 senior acima master
import datetime
anonasc = int(input('Digite o seu ano de nascimento: '))
idade = datetime.date.today().year - anonasc
print('Sua idade é {} anos' .format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFALTIL')
elif idade <=19:
    print('Sua categoria é JUNIOR')
else:
    print('Sua categoria é MASTER')

#desario do triangulo e seguimento de reta e omstrar qual triangulo é: equilatero todos os lados iguais Isoceles 2 lados iguais escaleno todos diferente
r1 = float(input('Digite um seguimento de reta:'))
r2 = float(input('Digite um seguimento de reta:'))
r3 = float(input('Digite um seguimento de reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Esses seguimentos PODEM formar um triangulo')
    if r1 == r2 == r3:
        print('E esse triangulo é EQUILATERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E esse triangulo é ISOCELES')
    else:
        print('E esse triangulo é ESCALENO')
else:
    print('Esses segmentos NAO PODEM formar um triangulo')

#Programa leia o peso e altura de uma pessoa e calculo o IMC e mostre  abixo de 18.5 abaixo do peso, entre 18.5 e 25 peso idela, 25 ate 30 sobrepeso, 30 a 40 obesidade acima 40 obesidade mosbida
kg = float(input('Qual seu peso em kg? '))
h = float(input('Qual sua altura em metros: '))

imc = kg / (h * h)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo de peso!')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')

#progama que calcula o valor a ser  pago por um produto consideranco seu preco normal e condicao de pagamento, a vista dinheiro/cheque 10% de desconto, a vista cartao 5% de desconto em ate 2x no cartao preco normal, 3x ou mais no cartao 20% de juros
print('{:=^40}'.format(' LOJA ALLAN '))
total = float(input('Preço das compras: R$'))
print('Formas de PAGAMENTO \n [1] À vista dinheiro/cheque \n [2] À vista cartão \n [3] 2x no cartão \n [4] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))

if opcao == 1:
    desconto = total * (10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(total, total - desconto))
elif opcao == 2:
    desconto = total * (5/100)
    print('Sua compra de R${:.2f} vai sair R${:.2f}'.format(total, total - desconto))
elif opcao == 3:
    print('Sua compra deu R${:.2f}'.format(total))
elif opcao == 4:
    parcel = int(input('Quantas parcelas? '))
    acrescimo = total * (20/100)
    valorparcel = (total + acrescimo) / parcel
    print('Sua compra sera parcelada em {} vezes com o valor de R${:.2f} a parcela no total de R${:.2f50}'.format(parcel, valorparcel , total + acrescimo))
else:
    print('Opcao INVALIDA')

#programa que computador jogue JOKENPO
import random
itens = ('Pedra','Papel','Tesoura')
print('Suas opções \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA')
opcao = int(input('Qual é sua JOGADA? '))
maquina = random.randint(0,2)
print('-=' * 10)
print('Computador jogou {}'.format(itens[maquina]))
print('O jogador jogou {}'.format(itens[opcao]))
print('-=' *10)
if maquina == opcao:
    print('O jogo EMPATOU')
elif maquina == 0 and opcao == 2:
    print('A maquina GANHOU')
elif maquina == 1 and opcao == 0:
    print('A maquina GANHOU')
elif maquina == 2 and opcao == 1:
    print('A maquina GANHOU')
else:
    print('Parabens VC GANHOU!')

'''

