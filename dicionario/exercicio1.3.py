time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador["name"] = str(input("Entre com o nome do jogador: "))
    tot = int(input(f'\n Qual a quantidade de partidas que {jogador["name"]} jogou? \n Resp.: '))
    partidas.clear()
    for c in range(0,tot):
        d = c+1
        partidas.append(int(input(f'Quantos gols na partida {d}?\n Resp.: ')))
    jogador["Gols"] = partidas[:]
    jogador["Total de gols"] = sum(partidas)
    time.append(jogador.copy())
    print(jogador)
    while True:
        continuar = str(input("Quer continuar? S/N \n")).upper()[0]
        if continuar in "SN":
            break
        print("Errado......Responda apenas sim ou não.")
    if continuar == "N":
        break
print(time,"\n")

while True:
    buscar = int(input("Entre com um indice para mostrar o jogador ou digite 500 para parar \nIndice =>"))

    if buscar == 500:
        break
    elif buscar >= len(time):
        print(f'Não temos jogador com indice {buscar}.')
    else:
        print("\n")
        print(f'O jogador {buscar} é o {time[buscar]["name"]} e por acaso ele fez {sum(time[buscar]["Gols"])} em {len(time[buscar]["Gols"])} partidas')
        print("\n")

        perg = int(input("Você quer saber quantos gols ele fez em cada partida? 1(sim) ou 2(não)"))

        if perg == 2:
            print("Tudo bem,sem problemas.")
        else:
            print("\n")
            r = 0
            for n1, n2 in enumerate(time[buscar]["Gols"]):
                print(f'No jogo {n1 + 1} ele fez {n2} gols.')