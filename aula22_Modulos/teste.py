from aula22_Modulos.utilidadescev import moeda
from aula22_Modulos.utilidadescev import dado

preco = dado.leiaDinheiros(f'Digite o preço: R$')
moeda.resumo(preco, 10, 5)

