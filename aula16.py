#16 - Tuplas
#lanche = (hamburguer,cerveja,pizza,pudim)
#print(lanche [2]) = pizza
#print(lanche [0:2] =ham,cerveja
#print(lanche[-1] = pudim
#len(lanche) = 4
#for c in lanche:
#   print(c) -> hamburget, depois cerveja, depois pizza, depois pudim, sai do for
#AS TUPLAS SAO >>>>IMUTAVEIS<<<
#
#NAO PRECISA DOS PARENDES SE QUISER
#lanche = ('Hamburger','Suco','Pizza','Pudim')
#print(lanche[0])
#print(len(lanche))

#print(sorted(lanche)) # EM ORDEM

#for comida in lanche: # sem as posiçoes
#    print(f'Eu vou comer {comida}')

#for cont in range(0, len(lanche)): # com posicao no caso o cont
#    print(cont)
#    print(lanche[cont])

#for pos, comida in enumerate(lanche): # com posicao
#    print(f'Comi {comida} e a posicao {pos}')

#a = (2,5,4)
#b = (5,8,1,2)
#c = a + b # junta
#d = b + a # junta diferente
#print(c)
#print(len(c))
#print(c.count(5)) # quantas vezes esta aparecendo o numero 5
#print(c.index(8)) # a posicao que esta o numero 8 pega a primeira ocorrencia
#print(c.index(2))
#print(c.index(2,1)) # depois da posicao 1 pois ja sabe que tem um na zero

#pessoa = ('Allan',28,'M','80.10') #aceita varios tipos de dados
#print(pessoa)
#del(pessoa) # APAGA TODA A TUPLA

'''
#72 Programa que tenha uma tupla totalmente preenchida com contagem por extenso de zero ate vinte. programa deve ler o numero pelo teclado e mostralo por extenso
contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
while True:
    numero = int(input('Digite um numero de 0 a 20: '))
    if 0 <= numero <= 20:
        opcao = ' '
        print(f'Seu numero é {contagem[numero]}')
        while opcao not in 'SN':
            opcao = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if opcao == 'N':
            break

#73 crie uma tupla com 20 primeiros colocados do campeonato brasieleiro na ordem de colocaca. depois mostre apenas os 5 primeiros. os 4 ultimos uma lista em ordem alfabetica, e em que posicao o time da chape esta na tabela
times = ('Bragantino','Atlético-GO','Sport','CRB','Coritiba','Botafogo-SP','Operário-PR','Ponte Preta','Cuiabá','América-MG','Paraná','Guarani','Brasil de Pelotas','Oeste','Vila Nova','Londrina','Criciúma','Vitória','São Bento','Figueirense')
print(f'Os 5 primeiros são: {times[0:5]}')
print(f'Os 4 ultimos e na zona de rebaixamento {times[-4:]}')
print(f'Ordem alfabetica dos time: {sorted(times)}')
print(f'O Coritiba esta na {times.index("Coritiba")+1} posicao')

#74 programa que gere 5 numeros aleatorios e coloque em uma tupla. depois disso mostre a listagem de numeros gerados e tbm o menor e o maior valor.
import random
# n = (random.randint(0,9),random.randint(0,9),random.randint(0,9), random.randint(0,9), random.randint(0,9))
ran1 = random.randint(0,9)
ran2 = random.randint(0,9)
ran3 = random.randint(0,9)
ran4 = random.randint(0,9)
ran5 = random.randint(0,9)
num =(ran1,ran2,ran3,ran4,ran5)
print(num)
print(f'O maior valor sorteado foi {max(num)} e o menor foi {min(num)}')

#75 Programa que leia 4 valores pelo teclado e guarde em uma tupla. no final mostre quantas vezes apareceu o numero 9 em que posicao foi digitado o primeiro valor 3, quais foram os numeros pares

val1 = int(input('Digite um valor: '))
val2 = int(input('Digite um valor: '))
val3 = int(input('Digite um valor: '))
val4 = int(input('Digite um valor: '))
valores = (val1,val2,val3,val4)
print(valores)
print(f'O numero 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O primeiro numero 3 esta na {valores.index(3)+1} posiçao')
else:
    print('O numero 3 nao foi digitado ')
for n in valores:
    if n % 2 == 0:
        print(f'Foi digitado {n} e ele é PAR')


#76 programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia, no final organize em forma tabular
listagem = ('Lapis',1.75,'Borracha',0.55,'Caderno', 15.00,'Penal',5.00,'Trasferidor',3.00,'Compasso',6.45,'Mochila',100.00,'Caneta',1.20,'Livros',55.50)
soma = 0
print('-' *40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>7.2f}')
        soma += listagem[pos]
print('-' *40)
print(f'{"Total":.<30}',end='')
print(f'R$ {soma:>7.2f}')

#77 crie uma tupla com varias palavras (SEM ACENTEO). depois mostrar para cada palvra quais sao as vogais
palavras = ('aprender','programar','python','linguagem','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
'''