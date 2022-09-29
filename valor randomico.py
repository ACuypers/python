
import json
import random


MaximoId = int(input('Digite o numero de quantas filiais vai acrescentar:'))
id = 1
numerocnpj = 1
while MaximoId > 0:

    valVendaBrutaItens = random.randrange(100000,30000000)
    valVendaBrutaAdicionais = random.randrange(10000,50000)
    valVendaBruta = random.randrange(100000,30000000)
    valCancelamentosItens = random.randrange(10000,150000)
    valCancelamentosAdicionais = random.randrange(100,1000)

    valDescontosItens = random.randrange(10000,150000)
    valDescontosAdicionais = random.randrange(100,1000)

    quantidadeTotalComandasPagas = random.randrange(10,2000)
    quantidadeTotalPessoasPagas = random.randrange(10,2000)

    numerocnpj = str(numerocnpj)

    resumoFinanceiro = {
                "valVendaBrutaItens": valVendaBrutaItens,
                "valVendaBrutaAdicionais": valVendaBrutaAdicionais,
                "valVendaBruta": valVendaBrutaItens + valVendaBrutaAdicionais,
                "valCancelamentosItens": valCancelamentosItens,
                "valCancelamentosAdicionais": valCancelamentosAdicionais,
                "valCancelamentos": valCancelamentosItens + valCancelamentosAdicionais,
                "valVendaEfetiva": (valVendaBrutaItens + valVendaBrutaAdicionais) - (valCancelamentosItens + valCancelamentosAdicionais),
                "valDescontosItens": valDescontosItens,
                "valDescontosAdicionais": valDescontosAdicionais,
                "valDescontos": valDescontosItens + valDescontosAdicionais,
                "valVendaLiquida": (valVendaBrutaItens + valVendaBrutaAdicionais) - (valCancelamentosItens + valCancelamentosAdicionais) - (valDescontosItens + valDescontosAdicionais),
                "quantidadeTotalComandasPagas": quantidadeTotalComandasPagas,
                "quantidadeTotalPessoasPagas": quantidadeTotalPessoasPagas
            }

    empresa = [
            {
                "id": id,
                "cnpj": "19.662.039/0001-" + numerocnpj,
                "nomeFantasia": "TESTE ENGENHARIA" + numerocnpj ,
                "resumoFinanceiro": resumoFinanceiro
            }
        ] 

    if id == 1:
        dados = {
            "intMes": 6,
            "intAno": 2022,
            "empresas": empresa
        }

        converter = json.dumps(dados, indent=4)
        
    else:
        with open ("exemplo1.json","a") as outfile:
            outfile.write(converter)
        converter = json.dumps(empresa, indent=4)

    numerocnpj = int(numerocnpj)   
    numerocnpj += 1
    MaximoId -= 1
    id += 1    