## Ordem de precedencia
## 1 ()
## 2 ** potenciacao
## 3 * / // %
## 4 + -
## Operadores Relacionais
## Atribuir a igualdade ==
## Atribuir a Diferente !=
## Atribuir Maior ou igual e Menor ou igual >= e <=
## Operadores Logicos (varias comparacoes ao mesmo tempo)
## AND OR NOT
"""
#Prgrama que calcula o antecessor e o sucessor
n = int(input ('Digite um numero'))
print('O numeor é {} o antecessor é {} o sucessor é {}' .format(n, n - 1,n + 1))
print(f'O numero é {n} o antecessor é {n-1} e o sucessot é {n+1}') ATUALIZACAO

#Programa que calcula o dobro ,triplo e a raiz
n = int(input('Digite um numer '))
print('O Dobro dele é {} o triplo e {} e a raiz {}'.format(n*2,n*3,n**(1/2)))

#Programa que faz a media de duas notas
n1 = float(input("Primeira Nota "))
n2 = float(input('Seguda nota '))
media = float((n1+n2) / 2)
print("Sua media é {}" .format(media))

#Programa que le valor em metro e converte para cm e milimitros
n = float(input('Valor em metros '))
print('Seu valor em cm é {} e em mm {}' .format(n*100, n*1000))

#Programa que leia um numero e mostre sua tabuada
n = int(input("Digite um numero para saber a tabuada "))
print("{} x 1 = {}".format(n,n*1))

#Programa que le quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar 1dolar = 3,27
din = float(input('Quanto de dinheiro vc tem na sua carteira? R$ '))
print('Voce pode comprar {:.2f} dolares' .format(din / 3.27))

#Programa leia a largura e altura e calcula a area e quantidade de tinta para pintala sabendo  que cada litro pinta 2m2
larg = float(input('Qual a Largura da parede '))
alt = float(input('Qual a Altura da parede '))
print('A Area da parede é {} e ira precisar de {} litro de tinta' .format(larg*alt, (larg*alt) / 2))

#Programa  preco de um produto e de 5% de desconto
preco = float(input('Qual o preco do produto '))
desco = preco*(5/100)
print('O preco original é {} e com desconto {}'.format(preco, preco-desco))

#Programa que mostre salario e o novo com o aumento de 15%
sal = float(input('Qual seu salario '))
aumen = sal*15/100
print('Seu salario antigo era {} e com aumento ficou {} '.format(sal, sal+aumen))
"""
