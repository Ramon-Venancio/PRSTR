#Modificador a lista:
nomes = ["Arthur", "Denilson", "Maria", "Ana"]
print("A lista atual é: ", nomes, "\n")

nome_a_alterar = input("Qual nome você gostaria de alterar?\n")

if (nome_a_alterar in nomes):
    posicao = nomes.index(nome_a_alterar)
    nome_novo = input("Digite o novo nome:\n")
    nomes[posicao] = nome_novo
    print(nomes)