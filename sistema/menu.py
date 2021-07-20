
from sistema.arquivo import *
from time import sleep


arq = 'bd.txt'
csv = 'athlete_even.csv'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema','Arquivo CSV'])
    if resposta == 1:
        #Opção de listar o conteudo do arquivo
        lerArquivo(arq)
        sleep(2)
    elif resposta == 2:
        #Opçao de cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(2)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema')
        break
    elif resposta == 4:
        lerArquivocsv(csv)
    else:
        cabeçalho('ERRO!Digite uma opçao valida')


