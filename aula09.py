## frase.count('o') conta quantas letras o tem na frase toda
##frase.find('deo') encontra quantas vezes o deo aparece e retorna o momento que começou a aparecer
## 'Curso' in frase é um operador que analisa se tem a palavra curso na frase
## frase.replace('A','B') muda todas as letras A por B
## upper maiusculo lower minisculo
## capitalize so o primeira letra fica maiuscula
## title onde tiver espaço a proxima letra fica maiuscula
## strip remove os espaço inuteis rstrip direito lstrip esquerda
## split divide a frase em outras listas
## '-'.join(frase) junta o que esta separado por espaço por -

##Programa leia o nome completo de uma pessoa e mostre o nome com todas as letras maiusculas , minusculas
##quantas letras ao todo sem considerar espaço e quantas leras tem o primeiro nome
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome maiusculo é: {}'.format(nome.upper()))
print('Seu nome minisculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)- nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados ex:1834 U:4 D:3 C:8 M:1
num = int(input('Digite um numero de 0 a 9999: '))
#num =str(num)
#print('Unidade {}'.format(num[3]))
#print('Dezena {}'.format(num[2]))
#print('Centena {}'.format(num[1]))
#print('Milhar {}'.format(num[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 %10

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

#Programa que leia nome de uma cidade e se ela começa com santo ou nao
cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

#Programa que leia um nome de uma pesssoa e diga se tem 'Silva' ou nao em qualquer posicao
nome = str(input('Digite seu nome: ')).strip()
print('SILVA' in nome.upper())

#Programa que leia uma frase e quantas vezes aparece a letra A, posição que ela aparece a primeira vez e a ultima vez
frase = str(input('Digite uma frase: ')).strip().upper()
##frase = frase.upper()
print('Na frase tem {} letras A'.format(frase.count('A')))
print('A posição do peimeiro A {} e o ultimo {}'.format(frase.find('A')+1, frase.rfind('A')+1))

#Programa que leia o nome completo de uma pessoa e mostre em seguida o nome e o ultimo nome separadamente ex: ana maria  de souza p:ana u:souza
nome = str(input('Digite seu nome completo: ')).strip().split()
##nome = nome.split()
print('Seu primeiro nome é {} '.format(nome[0]))
print('seu ultimo  nome é {} '.format(nome[len(nome)-1]))
"""


