numeri = int(input("Digite um numero de 0 a 9999\n"))

while numeri < 0 or numeri > 9999:
        print("Digito invalido")
        numeri = int(input("Digite novamente\n"))

numeri = str(numeri)
lista = list(numeri)

for r,x in enumerate(lista):
    if r == 0:
        print("Unidade:",x)
    elif r == 1:
        print("Dezena:",x)
    elif r == 2:
        print("Centena:",x)
    elif r == 3:
        print("Milhar:",x)