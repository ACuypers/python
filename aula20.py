#20 - Funções (Parte 1)
#def mostralinha():
#   print('--------------')
#
#mostralinha()
#print('AULA')
#mostralinha()
#
#def mensagem(msg):
#print('------------')
#print(msg)
#print('------------')
#
#mensagem('AULA')
#
#def contador(*num) >>> passar varios parametros vai criar uma TUPLA que nao sao alteradas
#contador(1,2,4)
#contador(1,5,6,7,8,9)
#
#def dobra(lst):
#pos = 0
#while pos < len(lst)
#lst[pos] *= 2
#pos += 1
#
#
#valores = [2,5,6,7,0,3]
#dobla(valores)
#print(valores)
#
#
#def soma (* valores) >>> DESEMPACOTAR VALORES
#   s = 0
#   for num in valores:
#       s += num
#   print(valores, s)
#
#soma(2,5)
#soma(2,5,6,7)

#96 programa que tenha uma funcao chamada area() que recebe as dimensoes de um terreno retangular (largura e compiemnteo) e mostre a area do terreno
'''
def area(largura,comprimento):
    a = largura * comprimento
    print(f'A area do terreno de {largura} X {comprimento} é de {a} m²')


#area(5,5)
lar = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(lar,comp)

#97 programa que tenha uma funcao escreva() que recebe um texto qualquer como parametro e mostre a msg com o tamanho adaptavel
def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)

escreva('Olá')
escreva('Allan')
escreva('Aula de python')

#98 programa que tenha uma funcao contador() que recebe 3 parametros inicio fim passo e realize a contagem. 1) de 1 ate 10   de 1 em 1 2) de 10 ate 0 de 2 em 2 3) personalizada
import time

def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if passo < 0:
        passo *= -1 #SE O PASSO FOR NEGATIVO
    if passo == 0:
        passo = 1 #SE O PASSO FOR 0
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            time.sleep(0.3)
            cont += passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}',end=' ')
            time.sleep(0.3)
            cont -= passo
        print('Fim')


contador(1,10,1)
contador(10,0,2)
print('Agora sua vez:')
i = int(input('Inicio: '))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i,f,p)

#99 programa que tenha uma funcao maior() que recebe vairos parametros com valores inteiros programa vai analisar qual e o maior
def maior(*num):
    maior = 0
    print('Analisando os valores passados:')
    for n in num:
        print(f'{n}', end=' ')
        if n > maior:
            maior = n
    print(f'Foram informados {len(num)}')
    print(f'O maior numero é {maior}')
    print('=-'*30)
maior(1,2,3)
maior(1,7,5,6,8,1,4)
maior()
'''
#100 programa que tenha uma lista chamada numeros e duas funcoes sorteia() e somapar(). a primeira sorteia 5 numeros e coloca dentro da lista e a segunda mostra a soma entre os valores pares sorteados.
import random
def sorteia(lista):
    while len(lista) < 5:
        gernum = random.randint(0,10)
        lista.append(gernum)
    #for cont in range(0,5):
        #lista.append(random.randint(0,10))

def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)

numeros = list()
sorteia(numeros)
print(numeros)
somapar(numeros)


