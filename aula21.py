# 21 - Funções (Parte 2)
#
#
#INTERACTIVE HELP
#help()
#quit
#
#
#DOCSTRINGS >> SUAS FUNÇOES COMENTADAS COMO O INTERACTIVE HELP
#   '''
#   AQUI VC COLOCA OS COMENTARIOS PARA AS DOCSTRINGS
#   '''
#EX>: contador(i,f,p)
#'''
#i > inicio
#f > fim
#p > passo
#'''
#
#help(contador)
#
#PARAMETROS OPCIONAIS
#
#somar(a,b,c)
#somar(a,b,c=0) C sera opcional e valera zero
#
#somar(2,3,4)
#somar(4,5)
#
#
#ESCOPO DE VARIAVEIS
#
#def funcao():
#n1 = 4 >>> Variavel LOCAL
#
#
#n1 = 2 >>>> Varivel GLOBAL
#print(n1 que eh global)
#
#global n1 >> sera sempre global
#
#
#RETORNANDO VALORE
#
#def somar(a,b,c)
#   s= a+b+c
#   return s
#
#resp1 = soma(3,2,7)
#resp2 = soma(4,5,6)
#resp3 = soma(6,6,4)
#print(resp1,resp2,resp3)
#
#
#101 Programa que tena funcao chamada voto() que vai receber paramatro o ano de nasc de uma pessoa retornando um valor literal indicando se uma pessoa tem voto negado opcional ou oubrigatorio nas eleicoes
#import datetime
'''
def voto(ano):
    import datetime ## SO VAI IMPORTAR NA FUNCAO
    idade = datetime.date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif 16 <= idade < 18 or idade > 70:
        return  f'Com {idade} anos: VOTO FACULTATIVO'
    else:
        return f'Com {idade} anos : VOTO OBRIGATORIO'



#print(voto(2000))
n = int(input('Em que ano você nasceu? '))
print(voto(n))

#102 programa que tenha funcao fatorial() que recebe 2 parametros: 1 indique o numero a calcular e outro chamado show que sera um valor logico(opcional) indicando se sera mostrado ou nao na tela o processo de calculo do fatorial
def fatorial(num,show=False):
    """
    >>> CALCULA O FATORIAL
    :param num: O numero a ser calculado
    :param show: Mostra em detalhes o calculo
    :return: Retorna o valor do fatrial
    """
    fat = 1
    for f in range(num,0,-1):
        if show:
            print(f ,end='')
            if f > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        fat *= f
    return fat


print(fatorial(5, False))
help(fatorial)

#103 programa que tenha funcao ficha() recebe 2 parametros opcionais: nome de um jogador e gols que ele marcou o programa sera capz de mostrar a fihca do jogador mesmo que algum dado nao tenha sido info
def ficha(jogador='<desconhecido>',gols=False):
        print(f'O jogador {jogador} fez {gols} gol (s) no campeonato')


n = str(input('Nome Jogador: '))
g = str(input('Numero de gols: '))
if g.isnumeric():
        g = int(g)
else:
        g = 0
if n.strip() == '':
        ficha(gols=g)
else:
        ficha(n,g)

#104 programa que tenha a funcao leiaint() que vai que funciona semelhante a funcao intput() so que fazendo validacao para aceitar apenas um valor numerico ex: n = leiaint('digite um n')
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Digite um numero valido')
        if ok:
            break
    return valor


n = leiaint('Digite um numero: ')
print(f'Você acabou de digitar o numero {n}')
'''
#105 programa que tenha funcao notas() que pode receber varias notas e retornar um dicionario com as inf: quantidade de notas , a maior, a menor , media.a situacao(opcional) add as docstrings

def notas(*n,sit=False):
#    '''
#    :param n: notas adicionadas
#    :param sit: situaçao que a media da turma ficou
#    :return: retona o total de notas, o maior valor , o menor valor , a media e a situaçao(opcional)
#    '''
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n)/len(n)
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'RUIM'
    return dados


#resp = notas(5,6,7,sit=True)
#print(resp)
#help(notas)

#106 faca minisistema que utilize o interactive help do python o usuario digita o comano e o manual vai apacer quando o usuario digital FIM o programa se encerra OBS use cores


def ajuda(com):
    help(com)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('=' *tam)
    print(f'  {msg}')
    print('=' *tam)

comando = ''
while True:
        titulo('SYSTEMA DE AJUDA PyHELP')
        comando = str(input('Função ou Biblioteca > '))
        if comando.upper() == 'FIM':
            break
        else:
            ajuda(comando)
titulo('ATE LOGO')

