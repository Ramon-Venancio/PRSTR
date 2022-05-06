lista = []
var = str(input("Escreva algo para por na lista:\n")).lower().capitalize()
lista.append(var)
opção = str(input("Digite s, se você quer continuar botando nomes na lista. Digite n, se você não quer continuar:\n"))

while opção == "s":
    print(f'Existem esses elementos na lista: {lista}.')
    var2 = str(input("Escreva outro nome para a lista: ")).lower().capitalize()
    while var2 in lista:
        print("Nome já existente.")
        var2 = str(input("Escreva outro nome para a lista: ")).lower().capitalize()
    lista.append(var2)
    opção = str(input("Digite s, se você quer continuar botando nomes na lista. Digite n, se você não quer continuar: "))

opção2 = str(input("Você quer deletar algum nome da sua lista? Digite s para sim ou n para não: "))

while opção2 == "s":
    print(f'Existem esses elementos na lista: {lista}.')
    var3 = str(input("Escreva algum nome da lista que você quer deletar: "))
    print("\n")
    if var3 in lista:
        posição = lista.index(var3)
        del lista[posição]
        print(f'Agora existem esses elementos na lista: {lista}.\n')
        opção2 = str(input("Você ainda quer deletar algum nome da sua lista? Digite s para sim ou n para não: "))
        print("\n")
    else:
        print("Nome não existente na lista.\n")