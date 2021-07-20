# 23 - Tratamento de Erros e Exceções
#
# Try
# OPERACAO
# Except
# falhou
#continue para continuar
# Else
# DEU CERTO
# Finally
# Certo/Falha ex FECHAR UM BD se der certo ou errado
#

# 113 - Rescreva a funcao leiaint() desafio 104 incluindo agora a possibilidade da digitacao de uma numero de tipo invalido e criar uma funcao leiafloat com mesma funcionalidade
'''
def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('ERRO! Digite um numero valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de Dados interrompida pelo usuario')
        else:
            return n

def leiafloat (msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um numero valido')
            continue
        except (KeyboardInterrupt):
            print('Entrada de Dados interrompida pelo usuario')
        else:
            return n

n1 = leiaint('Digite um numero inteiro: ')
n2 = leiafloat('Digite um numeor Real: ')
print(f'Você acabou de digitar o numero inteiro {n1} e o numero real {n2}')

# 114 - Codigo que testa se o site pudim esta acessivel
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu Erro')
else:
    print('Deu certo')
    print(site.read())
'''
# 115 - Sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de txt o sistema so tem 2 opçoes cadastrar uma nova pessoa e listar todas as pessoas cadastradas


