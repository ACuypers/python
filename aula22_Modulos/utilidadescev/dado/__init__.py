def leiaDinheiros(msg):
    while True:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO! \"{entrada}"\ Preço invalido!')
        else:
            return float(entrada)
            break
