geometric = str(input("Digite q, se você quer um quadrado ou t, se você quer um triângulo:\n"))

while geometric != "q" and geometric != "t":
    print("Opção inexistente. Digite novamente.")
    geometric = str(input("Digite q, se você quer um quadrado ou t, se você quer um triângulo:\n"))

if geometric == "q":
    lado1 = int(input("Digite o valor de um dos lados: "))
    lado2 = int(input("Digite o valor do outro lado: "))
    if lado1 == lado2:
        print("É realmente um quadrado.")
        print("A area do quadrado é:", lado1 ** 2)
    else:
        print("O que você escolheu não é um quadrado e sim um retângulo.")
        print("A area do retângulo é:", lado1 * lado2)
else:
    lado1 = int(input("Digite o valor de um dos lados: "))
    lado2 = int(input("Digite o valor outro do lado: "))
    lado3 = int(input("Digite o valor do ultimo lado: "))
    if lado1 == lado2 and lado1 == lado3:
        print("O seu triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("O seu triângulo é isóceles.")
    else:
        print("Seu triângulo é escaleno.")