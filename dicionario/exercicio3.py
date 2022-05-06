lista1 = []
lista2 = []

ctt1 = {}
ctt2 = {}

print("Contato 1")
while True:
    ctt1.clear()
    ctt1["Nome"] = input("Nome: ")
    ctt1["Conatato"] = input("Conatato: ")
    lista1.append(ctt1.copy())
    while True:
        resp = input("Quer continuar? S/N\n").upper()[0]
        if resp in "SN":
            break
        print("ERRO! Digite somente S/N")
    if resp == "N":
        print("\n")
        break

print("Contato 2")
while True:
    ctt2.clear()
    ctt2["Nome"] = input("Nome:")
    ctt2["Contato"] = input("Contato:")
    lista2.append(ctt2.copy())
    resp = input("Quer continuar? S/N\n").upper()
    b = len(resp)
    while (resp != "S" and resp != "N") and b > 1:
        resp = input("ERRO! Digite somente S/N\n").upper()
    if resp == "N":
        break
print("")