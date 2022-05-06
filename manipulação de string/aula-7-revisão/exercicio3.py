geometric = str(input("Digite q, se você quer um quadro, ou digite t, se você quer um triângulo:\n"))

while geometric != "q" and geometric != "t":
    print("Opção inexistente. Digite novamente.")
    geometric = str(input("Digite q, se você quer um quadro, ou digite t, se você quer um triângulo:\n"))

if geometric == "q":
    lado1 = int(input("Digite o lado: "))
    lado2 = int(input("Digite o segundo lado: "))
    if lado1 == lado2:
        print("Realmente é um quadrado.")
        area = lado1 ** 2
        print("A area é:",area)
    else:
        print("Não é um quadrado e sim um retângulo.")
        area = lado1 * lado2
        print("A area é:",area)