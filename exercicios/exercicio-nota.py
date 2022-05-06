nota = int(input("Digite uma nota de 0 a 10: "))

while nota > 10 or nota < 0:
    print("Numéro invalido.")
    nota = int(input("Digite novamente: "))