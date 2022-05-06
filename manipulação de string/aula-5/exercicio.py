b = "Denilson,Leonardo Vieira,Ramon Venancio,Robson"
lista = b.split(",")
quant = 0

for n in lista:
    comp = n.split(" ")
    v = len(comp)
    if v >= 2:
        quant += 1
print(quant)