## Cor no terminal
## exite o modulo colorize
## mas nesta aula usaremos o ANSI - ESCAPE SEQUENCE
## \033[        m
##\033[style, text, back m ex \033[0;33;44m
##STYLE: 0 SEM ESTILO,1 NEGRITO ,4 SUBLINHADO ,7 INVERTER
##TEXT: 30 BRANCO,31 VERMELHO, 32 VERDE, 33 AMARELO, 34 AZUL, 35 ROXO, 36 AZUL CLARO, 37 CINZA
##BACK: 40,41,42,43,44,45,46,47

print('\033[32;43m Olá Mundo!')
print('\033[32;44mOlá Mundo!\033[m')
nome = 'Allan'
print('Ola! {}{}{}'.format('\033[4;32m' , nome ,'\033[m'))