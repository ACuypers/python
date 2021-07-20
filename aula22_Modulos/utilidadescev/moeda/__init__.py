def aumentar(preco=0, taxa=0, formato= False):
    '''

    :param preco: parametro preco encaminhada
    :param taxa: parametro taxa encaminhado
    :param formato: True ira formatar em R$ caso contrario FALSE nao retona formatado
    :return: preco aumentado com o valor da taxa
    '''
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


def resumo(preco=0, taxaaum=0, taxadim=0, fotmato = False):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'PRECO ANALISADO: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobrar(preco,True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{taxaaum}% de aumento: \t{aumentar(preco,taxaaum,True)}')
    print(f'{taxadim}% de diminuiçao: \t{diminuir(preco,taxadim,True)}')
    print('-' * 30)