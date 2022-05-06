matriz = []
print("Escreva o tipo da sua matriz.")
i = int(input("Linhas: "))
j = int(input("Colunas: "))
print(f'Sua matriz é do tipo A{i}x{j}')
quant = i * j


for l in range(1,(i + 1)):
    sublista = []
    for c in range(1,(j + 1)):
        var = int(input(f'Digite o elemento a{l}{c}: '))
        sublista.append(var)
    matriz.extend([sublista])

for i,x in enumerate(matriz):
    print(x)