#15 - Interrompendo repetições while
#while true:
#   If
#       passo
#   if
#       pula
#   if
#       pega
#       break

#cont = 1
#while cont <= 10:
#    print(cont)
#    cont +=1
#print('Acabou')

#n = s = 0
#while True:
#    n = int(input('Digite um numero:'))
#    if n == 999:
#        break
#    s += n
#print('A soma é {}'.format(s))

# >>>>>>> print(f'A soma {s}')<<<<<<<<<< f strings
#print(f'A soma {s}')

#66 programa que leia varios numeros inteiros. so vai acabar quando o usuario digitar 999. mostrar quantos numeros foram digitados e a soma entre eles
'''
n= soma = count = 0
while True:
    n = int(input('Digite um valor(999 para parar): '))
    if n == 999:
        break
    soma += n
    count +=1
print(f'A soma dos numeros foi {soma} e foram digitados {count} valores')

#67 programa que mostre a tabuada de varios  numeros um de cada vez para cada valor digitado pelo usuario o programa sera parada quando o valor for negativo
tabu = count = 0
while True:
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    if tabu < 0:
        break
    while count < 10:  # for count in range (1,11):
        count += 1
        print(f'{tabu} X {count} = {tabu*count}')
    count = 0
print('Programa Tabuada ENCERRADO')

#68 programa que jogue par ou impar com o computador o jogo sera interrompido quando o jogador perder mostre o total de vezes de vitoria consecutivas
import random
computador = random.randint(0,10)
count = 0
while True:
    jogador = int(input('Digite um numero: '))
    print(computador)
    soma = jogador + computador
    parimp = str(input('Par ou Impar? [P/I]')).upper().strip()[0]
    if soma % 2 == 0:
        if parimp == 'P':
            print('Jogador ganhou')
            count +=1
        else:
            print('Computador ganhou')
            break
    else:
        if parimp == 'I':
            print('Jogador ganhou')
            count += 1
        else:
            print('Computador ganhou')
            break
print(f'GAME OVER o jogador ganhou {count} vezes')

#69 programa que leia idade sexo de varias pessoas a cada pessoa cadastrada o programa pergunta se quer continuar ou nao no final mostre quantas pessoas tem maior de 18 anos, quantos homem foram cadastrados quantas mulheres tem menos de 20 anos
counthome = countmulher = countidade = 0
while True:
    idade = int(input('Qual sua Idade? '))
    sexo =' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu Sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        countidade += 1
    if sexo == 'M':
        counthome += 1
    if sexo == 'F' and idade < 20:
        countmulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos é {countidade}')
print(f'O total de pessoas do sexo Masculino é {counthome}')
print(f'O total de Mulheres com menos de 20 anos é {countmulher}')

#70 programa que leia o nome e o preço de varios produtos o programa deve perguntar se quer ou nao continuar no final mostre total gasto na compra, quantos produtos custam mais de 1000 reais, nome do produto mais barato
print('='*30)
print('       LOJAO BARATAO')
print('='*30)
menor = countmil = count = soma = 0
barato = ''
while True:
    nomepro = str(input('Nome do Produto: '))
    precopro = float(input('Preço do Produto: R$'))
    count += 1
    soma += precopro
    if precopro > 1000:
        countmil += 1
    if count == 1:         # count == 1 or precopro < menor
        menor = precopro
        barato = nomepro
    else:
        if precopro < menor:
            menor = precopro
            barato = nomepro
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print('{:^40}'.format('FIM DO PROGRAMA'))
print(f'O TOTAL da compra foi {soma}')
print(f'Tem {countmil} produtos que custao mais de 1000')
print(f'O Produto {barato} com o menor preço é R${menor}')

#71 programa que simule o funcionamento de um caixa eletronico. no inicio pergunte ao usuario qual valor sera sacado(numero inteiro), e o programa vai infromar quantas cedulas de cada valor sera entregue obs: 50, 20, 10, 1
print('='*30)
print('{:^30}'.format('BANCO CUYPERS'))
print('='*30)
caixa = int(input('Qual o valor a quer sacadar? R$'))
total = caixa
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
'''
