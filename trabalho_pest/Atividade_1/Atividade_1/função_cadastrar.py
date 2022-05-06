from armazenamento import jogador,A,B,a_carteira,b_carteira
from rich import print

def cadastrar():
    global a_carteira
    global b_carteira
    global proximo
    print('-'*20)
    proximo = True
    while True:
        try:
            jogador["nome"] = input('Digite o nome do jogador: ').lower().capitalize()
        except KeyboardInterrupt:
            print("\n[#ff6f00]O usuário não quis mais cadastrar.[/]\n")
            proximo = False
            break
        else:
            if len(jogador["nome"]) == 0:
                print("[bold red]Valor invalido![/]")
            else:
                try:
                    jogador["nome"] = int(jogador["nome"])
                    print("[bold red]Só pode letras![/]\n")
                except:
                    nome_comp = jogador["nome"].split()
                    if len(nome_comp) < 2:
                        while True:
                            try:
                                composto = input(f'Digite um sobrenome para {jogador["nome"]}: ')
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            else:    
                                try:
                                    composto = int(composto)
                                    print("\n[bold red]Apenas letras![/]\n")
                                except (ValueError,TypeError):
                                    break
                            

                        if proximo == True:
                            try:  
                                nome_comp.append(composto)
                                nome_comp = nome_comp[0] + ' ' + nome_comp[1]   
                                jogador['nome'] = nome_comp.lower().capitalize()
                                break
                            except:
                                print("[bold red]Valor invalido![/]")
                        else:
                            break      
                    elif len(nome_comp) > 3:
                        print("[bold red]É permitido apenas três nomes e no minimo dois nomes![/]\n")
                    else:
                        break

    if proximo == True:
        while True:
            try:
                jogador['idade'] = int(input('Digite a idade do jogador: '))
            except (ValueError,TypeError):
                print("[bold red]Valor invalido! Apenas valores númericos![/]\n")
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                proximo = False
                break
            else:
                break

    if proximo == True:
        while True:
            try:
                jogador['nacionalidade'] = input("Digite a nacionalidae do jogador: ")
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar[/]\n")
                proximo = False
                break
            else:
                if len(jogador['nacionalidade']) == 0:
                    print("[bold red]Digite uma nacionalidade valida![/]\n")
                else:
                    try:
                        jogador['nacionalidade'] = int(jogador['nacionalidade'])
                        print("[bold red]Digite uma nacionalidade valida![/]\n")
                    except:
                        break

    if proximo == True:  
        while True:
            try:
                jogador['gols'] = int(input('Digite a quantidade de gols na ultima temporada: '))
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                proximo = False
                break
            except (ValueError,TypeError):
                print("[bold red]Valor invalido! Apenas valores númericos[/]\n")
            else:
                break

    if proximo == True:
        while True:
            try:
                jogador['salario'] = int(input('Digite o salario do jogador: '))
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                proximo = False
                break
            except (ValueError,TypeError):
                print("[bold red]Valor invalido! Apenas valores númericos.[/]\n")
            else:
                break

    if proximo == True:
        while True:
            try:
                time = input("Qual time o jogador pertence(A/B)?: ").upper()
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                proximo = False
                break
            else:
                if time == 'A':
                    a_carteira[0] = a_carteira[0] + jogador['salario']
                    A.append(jogador.copy())
                    break
                elif time == 'B':
                    b_carteira[0] = b_carteira[0] + jogador['salario']
                    print(b_carteira)
                    B.append(jogador.copy())
                    break
                else:
                    print("[bold red]Valor invalido![/]\n")
