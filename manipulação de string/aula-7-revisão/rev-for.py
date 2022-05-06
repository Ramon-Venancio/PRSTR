#O range serve para gerar uma sequência de numeros inteiros dentro de um intervalo determinado.
for item in range(10):
    print(item)

print("\n" * 2)

for item in range(9, -1, -2):
    print(item)

print("\n")
nomes = ["Pedro", "João", "Leticio"]
for n in nomes:
    print(n)
print("Fora do for?","\n")

for item in range(0, len(nomes), 2):
    print(nomes[item])