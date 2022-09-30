import json
import random


MaximoId = int(input('Digite o numero de quantas filiais vai acrescentar:'))
id = 1

while MaximoId > 0:

    quantidadeTotalComandasPagas = random.randrange(10,2000)
    quantidadeTotalPessoasPagas = random.randrange(10,2000)
    
    resumoFinanceiro = {
                "valVendaBrutaItens": 69945.18,
                "valVendaBrutaAdicionais": 0,
                "valVendaBruta": 69945.18,
                "valCancelamentosItens": 60008.19,
                "valCancelamentosAdicionais": 0,
                "valCancelamentos": 60008.19,
                "valVendaEfetiva": 129953.37,
                "valDescontosItens": 83.2,
                "valDescontosAdicionais": 495.57,
                "valDescontos": 578.77,
                "valVendaLiquida": 9358.22,
                "quantidadeTotalComandasPagas": quantidadeTotalComandasPagas,
                "quantidadeTotalPessoasPagas": quantidadeTotalPessoasPagas
    }

    dados =	{
        
                "id": id,
                "cnpj": "38.436.516/0001-56",
                "nomeFantasia": "TESTE ENGENHARIA",
                "resumoFinanceiro": resumoFinanceiro
    }

    if id == 1:
        cabecalhoJson = {
            "intMes": 6,
            "intAno": 2022,
            "empresas": dados
        }

        converter = json.dumps(cabecalhoJson, indent=4)
        
    else:
        with open ("exemplo.json","a") as outfile:
            outfile.write(converter)
        converter = json.dumps(dados, indent=4, separators=(', ',':'))
        # Mudei de W para a merda do A e começou a escrever correto
        #with open ("exemplo.json","a") as outfile:
            #outfile.write(converter)

    MaximoId -= 1
    id += 1
