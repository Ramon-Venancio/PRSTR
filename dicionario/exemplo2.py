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
        partidas.append(int(input(f'Quantos gols na partida {d}?\n Resp.:')))
    jogador["Gols"] = partidas[:]
    jogador["Total de gols"] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input("Quer continuar? S/N \n")).upper()[0]
    
    if continuar == "S":
    elif continuar == "N":
    
print(jogador)