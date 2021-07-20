"""
import math
num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num , raiz))

##Programa que leia um numero Real e mostre a tela a porcao inteira ex digite um numero 6.127 e a parte inteira é 6
import math
num = float(input('Digite um numero: '))
print('O numero é {} e a parte inteira é {} '.format(num, math.trunc(num)))

##Programa que leia o comprimento do cateto oposto e o adjacente de um tri ret calcule a hipotenusa
import math
catops = float(input('Digite o cateto oposto'))
catadj = float(input('DIgite o cateto adjacente'))
print('O cateto oposto é {} e o adjacente {} e sua hipotenusa {}'.format(catops,catadj ,math.hypot(catadj,catops)))
##Programa que leia um angulo qualquer e mostre o valor do seno cosseno e tang
import math
ang = float(input('Digite um angulo: '))
print('O angulo digitado é {} seu seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(ang, math.sin(math.radians(ang)),math.cos(math.radians(ang)),math.tan(math.radians(ang))))

##Programa que sorteia um dos 4 alunos para apagar o quadro.Faca um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido
import random
n1 = input('Primeiro aluno ')
n2 = input('Segundo aluno ')
n3 = input('Terceiro aluno ')
n4 = input('Quarto aluno ')
lista = [n1,n2,n3,n4]
print('O aluno escolhido é {} '.format(random.choice(lista)))

##Programa que sortea a ordem de apresentacao de trabalhos dos alunos. Leia o nome dos 4 alunos e mostre a ordem sorteada
import random
n1 = input('Aluno 1')
n2 = input('Aluno 2')
n3 = input('Aluno 3')
n4 = input('Aluno 4')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem sera {}' .format(lista))
"""
##Programa que abra e reproduza audio MP3
import pygame
##file = 'a.mp3'
pygame.mixer.init()
pygame.mixer.music.load('a.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



