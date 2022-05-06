cadastro = dict()
controle = list()
edicao = dict()
elemento = dict()

perg = int(input("[1] Para cadastrar produto\n[2] Para editar produto\n->"))

while perg == 1 or finalizador == "S":
    cadastro.clear()
    produto = str(input("Digite o nome do produto: "))
    cadastro["Produto"] = produto
    preço = float(input("Digite o preço: R$"))
    cadastro["Preço"] = preço
    quantidade = int(input("Digite a quantidade de produtos: "))
    cadastro["Quantidades"] = quantidade
    elemento[produto] = preço,quantidade

    controle.append(cadastro.copy())
    finalizador = str(input("Quer cadastrar outro produto? S - sim ou N - não.\n")).upper()[0]
    print("\n")

    while finalizador != "S" and finalizador != "N":
        finalizador = str(input("O que você escreveu está incorreto. escreva S para sim ou N para não.\n")).upper()[0]

    if finalizador == "N":
        print("-"*65)
        print(f'{"Quantidade":<} {"Produto":^} {"Preço":>}')
        for x,y in enumerate(controle):
            print(f'{controle[x]["Quantidades"]:<10} {controle[x]["Produto"]:<7.5} {controle[x]["Preço"]:<5.3}')
        break