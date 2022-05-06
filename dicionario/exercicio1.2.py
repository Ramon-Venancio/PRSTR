#O enumerate joga um valor para duas variaves.
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

print("-"*30)
print("Cod", end = '')

for c in jogador.keys():
    print(f'{c:<15}', end = '')
for i, d in enumerate(time):
    print(f'{i:>3}', end = '')

    for v in d.values():
        print(f'{str(v):<15}', end = '')
    print()
print("-"*30)
print(time)