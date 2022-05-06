#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome = str(input("Escreva seu nome: "))
soma = 0

mai = nome.upper()
minu = nome.lower()
print(mai)
print(minu)
palavras = nome.split()

for x in palavras:
    count = len(x)
    soma += count
print("A quantidade de letras é",soma)

let1 = len(palavras[0])
print("A quantidade de letras no primeiro nome é",let1)