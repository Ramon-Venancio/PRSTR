lista = []
var = str(input("Escreva algo par por na lista:\n")).lower().capitalize()
lista.append(var)
opção = str(input("Digite s, se você quer continuar botando nomes na lista. Digite n, se você não quer continuar:\n"))

while opção == "s":
    print(f'Existem esses elementos na lista: {lista}.')
    var2 = str(input("Escreva outro nome para a lista: ")).lower().capitalize()
    while var2 in lista:
        print("Nome já existente.")
        var2 = str(input("Escreva outro nome para a lista: ")).lower().capitalize()
    lista.append(var2)
    opção = str(input("Digite s, se você quer continuar botando nomes na lista. Digite n, se você não quer continuar:\n"))
