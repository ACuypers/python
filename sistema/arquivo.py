from sistema.funcoes import *
import csv

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criacao do arquivo')
    else:
        print(f'Arquivo {nome} criado')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def lerArquivocsv(nome):
    try:
        ficheiro = open(nome, 'r')
        ler = csv.reader(ficheiro, delimiter=';')
         #ficheiro = csv.reader(open(nome, 'r'), delimiter=';')

        for linha in ler:
            print("ID:", linha[0], " - Nome:", linha[1], " - Sex:", linha[2], "Idade", linha[3], "- Altura", linha[4],
            "- Peso", linha[5], "- Time", linha[5], "- NOC", linha[6], " - Jogos", linha[7], "- Ano",linha[8],
            "- Temporada",linha[9],"- Cidade",linha[10],"- Esporte",linha[11], "- Evento",linha[12],"- Medalha",linha[13])
    finally:
        ficheiro.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro')
    else:
        try:
            a.write(f'{nome} ; {idade}\n')
        except:
            print('Houve um erro na escrita dos dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()


