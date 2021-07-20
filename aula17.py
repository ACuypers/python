#17 - Listas (Parte 1)
#SAO MUTAVEIS
#lista = []
#lanches = ['hamburguer','suco','pizza','pudim']
#lanches[3] = 'picole'
#lanches = ['hamburguer','suco','pizza','picole']
#Adicionar na lista usa o APPEND lanche.append = 'cook' ( ele vai para o final da lista)
#Adicionar na lista usando o INSERT(0,'cachorro quente') adidiona ele no ZERO
#Apagar elementos del lanche[3] ou lanche.pop(3) lanche.pop()>> normalmente o pop e para remover o ultimo valor, mas pode passar o parametro e remover o que esta na posiçao
#lanche.remove('pizza)>>> esse indica o valor que quer eliminar
#if 'pizza' in lanche:
#   lanche.remove('pizza') >>>> SO VAI REMOVER SE TIVER NA LISTA, ai nao retorna erro
#
#PODE SE CRIAR LISTAS APARTIR DE RANGE
#valores = list(range(4,11))
#
#valor.sort() ORDENA A LISTA
#valor.sort(reverse=True) ORDENA A LISTA do MAIOR PARA O menor
#len(valores) conta quantos valores tem na lista
#
#
#valores = []
#valores.append(5)
#valores.append(7)
#valores.append(8)

#DIGITAR UM VALOR E COLOCAR EM UMA LISTA
#for cont in range(0,5):
#    valores.append(int(input('Digite um valor: ')))
#TER A POSICAO E O VALOR DENTRO DE UMA LISTA
#for c , v in enumerate(valores):
#    print(f'Na posicao {c} encontrei o valor {v}')
#print('Cheguei no final da lista')

#a = [1,3,6,8]
#b = a >>> CRIA UMA LIGACAO ENTRE LISTAS SE MUDAR UM VALOR EM B MUDA EM A
#b = a[:] >> CRIA UMA COPIA B NAO TEM LIGACAO NENHUMA COM A

#78programa que leia 5 valores numericos e guarde em uma lista no final mostre qual e maior e menor e suas respectivas posiçoes
'''
listvalor = []
#n = 0
#while n != 5:
#    valor = listvalor.append(int(input('Digite um valor: ')))
#    n = len(listvalor)
#listvalor = sorted(listvalor)
#print(f'O MAIOR valor é {listvalor[-1]} e o menor valor é {listvalor[0]}')
maior = menor = 0
for count in range(0,5):
    listvalor.append(int(input(f'Digite um valor para a Posição {count}: ')))
    if count == 0:
        maior = menor = listvalor[count]
    else:
        if listvalor[count] > maior:
            maior = listvalor[count]
        if listvalor[count] < menor:
            menor = listvalor[count]
print('=-'*30)
print(listvalor)
print('=-'*30)
print(f'O MAIOR valor {maior}')
for i, v in enumerate(listvalor):
    if v == maior:
        print(f'{i}...')
print(f'O menor valor {menor}')
for i, v in enumerate(listvalor):
    if v == menor:
        print(f'{i}...')
#print(f'Na posicao {count} encontrei o valor {v}')

#OUTRA SOLUCAO USANDO OS METODOS MAX E MIN E INDEX
#lista = []
#posicao_maior = []
#posicao_menor = []
#for p in range(0, 5):
#    val = int(input(f'Digite um valor na posição {p}: '))
#    lista.append(val)
#for posicao, valores in enumerate(lista):
#    if valores == max(lista):
#        posicao_maior.append(posicao)
#    if valores == min(lista):
#        posicao_menor.append(posicao)
#print(f'Você digitou os valores {lista}')
#print(f'O maior valor da lista é {max(lista)}, nas posições {posicao_maior}')
#print(f'O menor valor da lista é {min(lista)}, nas posições {posicao_menor}')

#79 programa que usuario digite valores numericos e cadstre em uma lista. caso o numero esteja la dentro ele nao sera cadastrado. no final sera mostrado os valores unicos em ordem crescente
valor = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
        print('Valor adicionado')
    else:
        print('Valor DUPLICADO')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break
print(valor)
valor.sort()
print(valor)

#80 programa que o usuario digite 5 valores numericos e cadastre em uma lista ja na posicao correta sem usar o sort. no vinal mostre a lista ordenado
valore = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0: # se o numero for o primeiro valor a ser add
        valore.append(n)
    elif n > valore[len(valore)-1]: # se o numero é maior que o ultimo da lista
        valore.append(n)
    else:
        pos = 0
        while pos < len(valore): # ele vai da primeira posicao da lista ate a a ultima
            if n <= valore[pos]: # se o numero é maior ou igual o numero que quero inserir
                valore.insert(pos,n)
                break
            pos += 1
print(valore)

#81 programa que leia varios numero e coloque em uma lista. dpeois mostre quantos numeros foram digitados lista em ordem decrescente se o valor 5 foi digitado ou nao
valor = []
count = 0
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)
    count += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if opcao == 'N':
        break
##MELHOR SOLUCAO
## if 5 in valor:
##    print('TEM O VALOR 5')
pos = 0
while pos < len(valor):
    if n == 5:
        print('Tem o numero 5')
        break
    else:
        print('Nao tem o numero 5')
        break
    pos += 1
print(valor)
valor.sort(reverse=True)
print(valor)
print(f'Foram digitados {count} valores') # len(valores)

#82programa que leia vareio numeros e coloque em uma lista. depois crie 2 listas extras que vao conter os numeros pares e impares   no final mostre as 3 listas
valor = []
valorpar = []
valorimp = []
while True:
    n = int(input('Digite um valor: '))
    valor.append(n)
    if n % 2 == 0:
        valorpar.append(n)
    else:
        valorimp.append(n)
    opcao = str(input('Deseja continuar S/N? ')).upper()
    if opcao in 'N':
        break
print(valor)
print(valorpar)
print(valorimp)
## for i, v in enumerate(valor):
##      if v % 2 == 0 PAR
##      else IMPAR

#83programa que usuario digite uma expressao que use parentes o programa deve ANALISAR a expresao e ver se tem ou nao parentes aberto e fehcado.
expre = str(input('Digite uma expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta ok')
else:
    print('Esta errado')
'''