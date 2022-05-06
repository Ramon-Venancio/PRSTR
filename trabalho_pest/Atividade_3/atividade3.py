contatos = {}
chip_1 = []
chip_2 =[]
backup = []
emails_chip_1 = []
emails_chip_2 = []

def menu():
    while True:
        try:
            opção = int(input(f'O que você quer fazer?\n{"-"*20}\n[1]Cadastrar_contato\n[2]Editar_contato\n[3]Fazer_backup\n{"-"*20}\nDigite o que você quer fazer: '))
        except (ValueError,TypeError):
            print("\nValor invalido!\n")
        except KeyboardInterrupt:
            print("\nAté mais.")
            break
        else:
            if opção > 3 or opção < 1:
                print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')
            else:
                if opção == 1:
                    Cadastrar_contato()
                    break
                elif opção == 2:
                    print("Em andamento.")
                    break
                elif opção == 3:
                    print("Em andamento.")
                    break

def Cadastrar_contato():
    print("\nOlá\n")
    while True:
        contatos.clear()
        try:
            contatos["Nome"] = input("Digite o nome do contato: ").title()
        except KeyboardInterrupt:
            print("\nAté mais.")
            proximo = False
        else:
            if (len(contatos["Nome"])) == 0:
                print("\nNão pode pode deixar o nome vazio!\n")
                proximo = "vazio"
            else:
                proximo = True

        while proximo == True:
            try:
                contatos["Telefone"] = input("Digite deacordo com isso:\nDDD (9)NNNN NNNN\n----------\nDDD - Área geografica(Sem parêntese.)\n(9) - Se o telefone for movel\nNNNN - Número\n----------\nDigite o numero do contato: ")
            except KeyboardInterrupt:
                print("\nO usuário não quis mais continuar.")
                proximo = False
            else:
                separador = contatos["Telefone"].split()
                if len(separador) == 1:
                    if len(separador[0]) == 3:
                        print(f'\n{"-"*20}\nNúmero publico.\n{"-"*20}\n')
                        break
                    else:
                        print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')
                elif len(separador) == 3:
                    if (len(separador[0]) == 2) and (len(separador[1]) == 5 or len(separador[1]) == 4) and (len(separador[2]) == 4):
                        numero = contatos["Telefone"]
                        contatos["Telefone"] = separador[0] + separador[1] + separador[2]
                        quant = len(contatos["Telefone"])
                        try:
                            contatos["Telefone"] = int(contatos["Telefone"])
                        except:
                            print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')
                        else:
                            if quant == 11 and (numero[3] == "9" or numero[3] == "8"):
                                contatos["Telefone"] = numero
                                print(f'\n{"-"*20}\nO número é movel\n{"-"*20}\n')
                                break
                            elif quant == 10 and (numero[3] == "5" or numero[3] == "2" or numero[3] == "3" or numero[3] == "4"):
                                contatos["Telefone"] = numero
                                print(f'\n{"-"*20}\nO número é fixo\n{"-"*20}\n')
                                break
                            else:
                                print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')
                    else:
                        print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')
                else:
                    print(f'\n{"-"*20}\nErro: Número invalido!\n{"-"*20}\n')

        while proximo == True:
            try:
                email = input("Digite seu email: ")
            except KeyboardInterrupt:
                print("\nO usuário não quis mais continuar.")
                proximo = False
                break
            else:
                if len(email) == 0:
                    print("\nNão pode deixar o E-mail vazio!\n")
                else:
                    verificador = email.split("@")
                    if len(verificador) != 2:
                        print("\nE-mail invalido!\n")
                    else:
                        contatos["E-mail"] = email
                        break

        while proximo == True:
            try:
                perg_chip = int(input("Em qual chip você quer botar o contato?\n[1]Chip_1\n[2]Chip_2\n"))
            except (ValueError,TypeError):
                print("Erro: valor invalido.")
            except KeyboardInterrupt:
                print("\nAté mais.")
                proximo = False
                proximo = False
                break
            else:
                if perg_chip == 1:
                    chip_1.append(contatos.copy())
                    emails_chip_1.append(contatos["E-mail"])
                    break
                elif perg_chip == 2:
                    chip_2.append(contatos.copy())
                    emails_chip_2.append(contatos["E-mail"])
                    break
                else:
                        print("Valor invalido!")
        if len(chip_1) == 2 and chip_1[0]["Nome"] == contatos["Nome"]:
            contatos.update(contatos)
        elif len(chip_2) == 2 and chip_2[0]["Nome"] == contatos["Nome"]:
            contatos.update(contatos)
        else:
            pass
        if proximo == True:
            try:
                perg = input("Você quer continuar? S(sim) ou N(não)\n").capitalize()
            except KeyboardInterrupt:
                print("\nAté mais.")
                proximo = False
            while proximo == True:
                try:
                    perg = int(perg)
                    perg = input("Digite somente letras!\n")
                except (ValueError,TypeError):
                        break
                except KeyboardInterrupt:
                    proximo = False
                    print("\nAté mais.")
                    break
            if proximo == True:
                while perg != "S" and perg != "N":
                    perg = str(input("Valor errado. Digite somente S ou N:\n")).capitalize()
                    
                if perg == "N":
                    break
                else:
                    pass
            else:
                break
        else:
            if proximo == "vazio":
                pass
            else:
                break


def editar():
    escolha = int(input("Qual chip você quer editar(1 ou 2):\n"))
    while escolha != 1 and escolha != 2:
        escolha = int(input("Digite um chip válido(1 ou 2):\n"))
    if escolha == 1:
        if len(chip_1) == 0:
            print("O chip está vázio")
            menu()
    elif escolha == 2:
        if len(chip_2) == 0:
            print("O chip está vázio")
            menu()
    else:
        pass   

    
menu()
print(f'Chip_1:{chip_1}\nChip_2:{chip_2}')