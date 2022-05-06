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
print(time)

pergunta = str(input("Escreva o que você quer mudar: ")).lower()
decição = False
print("\n")

for x in time:
    if pergunta == "nome":
        print(x)
        pergunta2 = str(input(f'Você quer mudar o nome desse dicionário? Digite s para sim ou n para não.\nResp.: ')).lower()
        
        while pergunta2 != "s" and pergunta2 != "n":
                pergunta2 = str(input("Resposta invalida. Digete novamente.\nResp.: "))
        
        if pergunta2 == "s":
            nome_novo = str(input("Digite um nome para subtituir: "))
            x["name"] = nome_novo
            decição = True
    elif pergunta == "gols":
        for r in range(0,tot):
            r += 1
            pergunta2 = str(input(f'Você quer mudar o gol da partida {r}? Digite s para sim ou n para não.\nResp.: ')).lower()

            while pergunta2 != "s" and pergunta2 != "n":
                pergunta2 = str(input("Resposta invalida. Digete novamente.\nResp.: "))
            
            if pergunta2 == "s":
                numeri = int(input("Digite a quantidade que você quer: "))
                r -= 1
                x["Gols"][r] = numeri
                x["Total de gols"] = sum(x["Gols"])
                r += 1
                decição = True
            else:
                r += 1
if decição == True:
    print(time)
else:
    print("Informação não encontrada.")