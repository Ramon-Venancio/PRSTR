nome = "continuar"
lista = [123,"xyz","milion",888]
print("A lista é:\n", lista)
opção = int(input("Digite qual opção você quer?\nOpção 1:Só letra ou \nopção:Só número 2\n")) 


if opção == 1:
    nome_l = input("Qual nome você quer saber o numero de repetições?\n")
    if nome_l in lista:
        while nome == "continuar":
            count = lista.count(nome_l)
            perg = input("Você quer continuar ou parar?\n")
            if perg == "parar":
                nome = "parar"
            else:
                nome_l = input("Qual nome você quer saber o numero de repetições?\n")
                nome_n = int(nome_l)
    else:
        print("O que você escolheu não exite na lista")
else:
    nome_l = input("Qual nome você quer saber o numero de repetições?\n")
    nome_n = int(nome_l)

    if nome_l in lista or nome_n in lista:
        while nome == "continuar":
            count1 = lista.count(nome_n)
            count2 = lista.count(nome_l)
            sc = count1 + count2
            print(sc)
            perg = input("Você quer continuar ou parar?\n")
            if perg == "parar":
                nome = "parar"
            else:
                nome_l = input("Qual nome você quer saber o numero de repetições?\n")
                nome_n = int(nome_l)
    else:
        print("O que você escolheu não exite na lista")