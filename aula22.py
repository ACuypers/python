#22 - Módulos e Pacotes
#
#MODULARICACAO - DIVIDIR UM PROGRAMA GRANDE
#
#import uteis (TEM AS FUNÇOES FATORIA,DOBRO, TRIPLO EM OUTRO ARQUIVO)
#
#num = int(input('Digite um numero'))
#fat = uteis.fatorial(num)
#print(f'o fatorial de {num} é {fat}')
#print(f'o dobro de {num} é {uteis.dobro(num)}')
#
#
#PACOTES - PASTA QUE CONTEM MODULOS, caso UTEIS tivese muitas funçoes
#separar por numeors, strigs,datas,cores
#-----criar uma pasta dentro de UTEIS se cira um pacotes
#
#
#107 Crie um modulo moeda.py que tenha as funçoes aumentar diminuir dobrar e metade, programa que importe esse modulo e utilize
#moeda.py
'''
def aumentar(n):
    aum = ((n * 10) / 100) + n
    return print(f'Aumentando 10%, temos R$ {aum}')
def diminuir(n):
    dim = n - ((n * 10) / 100)
    return print(f'Diminuindo 10%, temos R$ {dim}')
def dobrar(n):
    dob = n * 2
    return print(f'O dobro de {n} é R$ {dob}')
def metade(n):
    met = n / 2
    return print(f'A metade de {n} é R$ {met}')

#teste.py
from aula22_Modulos import moeda

preco = float(input('Digite o preço: R$: '))
taxa = int(input('Digite a taxa: '))
moeda.aumentar(preco, taxa)
moeda.diminuir(preco, taxa)
moeda.dobrar(preco)
moeda.metade(preco)


#
#108 adapte o desafio 107 crie uma funcao adicional chamada moeda() que consiga mostrar o valor formatado monetario
moeda.py
def aumentar(preco=0, taxa=0):
    aum = preco + ((preco * taxa) / 100)
    return aum
def diminuir(preco=0,taxa=0):
    dim = preco - ((preco * taxa) / 100)
    return dim
def dobrar(preco=0):
    dob = preco * 2
    return dob
def metade(preco=0):
    met = preco / 2
    return met
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


teste
from aula22_Modulos import moeda

preco = float(input('Digite o preço: R$: '))
taxa = int(input('Digite a taxa: '))
print(f'Aumentando {taxa}%, temos {moeda.moeda(moeda.aumentar(preco,taxa))}')
print(f'Diminuindo {taxa}%, temos {moeda.moeda(moeda.diminuir(preco, taxa))}')
print(f'O dobro de {preco} é {moeda.moeda(moeda.dobrar(preco))}')
print(f'A metade de {preco} é {moeda.moeda(moeda.metade(preco))}')

#109 modifique o desafiio 107 para que eles aceitem um parametro a mais, informando se o valor retontnado  por eles vai ser ou nao formatado pela funcao moeda()
#moeda.py
def aumentar(preco=0, taxa=0, formato= False):
    aum = preco + ((preco * taxa) / 100)
    return aum if formato is False else moeda(aum)
def diminuir(preco=0,taxa=0, formato= False):
    dim = preco - ((preco * taxa) / 100)
    return dim if formato is False else moeda(dim)
def dobrar(preco=0, formato= False):
    dob = preco * 2
    return dob if formato is False else moeda(dob)
def metade(preco=0, formato= False):
    met = preco / 2
    return met if formato is False else moeda(met)
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
teste.py
from aula22_Modulos import moeda

preco = float(input('Digite o preço: R$: '))
taxa = int(input('Digite a taxa: '))
print(f'Aumentando {taxa}%, temos {moeda.aumentar(preco,taxa,True)}')
print(f'Diminuindo {taxa}%, temos {moeda.diminuir(preco, taxa, True)}')
print(f'O dobro de {preco} é {moeda.dobrar(preco, True)}')
print(f'A metade de {preco} é {moeda.metade(preco, True)}')

#110 adicione ao modulo moeda.py uma funcao chamada resumo() mostra informaçoes
#moeda.py
def aumentar(preco=0, taxa=0, formato= False):
    #'''

    #:param preco: parametro preco encaminhada
    #:param taxa: parametro taxa encaminhado
    #:param formato: True ira formatar em R$ caso contrario FALSE nao retona formatado
    #:return: preco aumentado com o valor da taxa
    #'''
    #aum = preco + ((preco * taxa) / 100)
    #return aum if formato is False else moeda(aum)
def diminuir(preco=0,taxa=0, formato= False):
    dim = preco - ((preco * taxa) / 100)
    return dim if formato is False else moeda(dim)
def dobrar(preco=0, formato= False):
    dob = preco * 2
    return dob if formato is False else moeda(dob)
def metade(preco=0, formato= False):
    met = preco / 2
    return met if formato is False else moeda(met)
def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
def resumo(preco=0, taxaaum=0, taxadim=0, fotmato = False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'PRECO ANALISADO: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobrar(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    #print(f'{taxaaum}% de aumento: \t{aumentar(preco,taxaaum,True)}')
    print(f'{taxadim}% de diminuiçao: \t{diminuir(preco,taxadim,True)}')
    print('-' * 30)


#teste.py
from aula22_Modulos import moeda

preco = float(input('Digite o preço: R$: '))
moeda.resumo(preco, 10, 5)
'''
#111 crie um pacote utilidadesCeV que tenha 2 moduloes moedas e dados, trasfira todas as funcoes  dos desafio anteriores para o primeiro pacote
#criou o init.py moeda
#112 dentro do pacote utilidadadesCeV temos um modulo chamado dados crie uma funcao chamada leiaDinheiros() que seja capaz de funcionar como uma funcao input com mais uma validacao de dados para aceitar apenas valores monetarios

'''
