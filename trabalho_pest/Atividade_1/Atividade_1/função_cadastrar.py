from armazenamento import jogador,A,B,a_carteira,b_carteira
from rich import print

def cadastrar():
    global a_carteira
    global b_carteira
    global proximo
    global afirm
    print('-'*20)
    proximo = True
    while True:
        afirm = True
        try:
            jogador["nome"] = input('Digite o nome do jogador: ').lower().capitalize()
        except KeyboardInterrupt:
            print("\n[#ff6f00]O usuário não quis mais cadastrar.[/]\n")
            proximo = False
            break
        else:
            comp = jogador["nome"].split(" ")

            for i,n in enumerate(comp):
                try:
                    int(n)
                except:
                    for m in n:
                        try:
                            int(m)
                        except:
                            pass
                        else:
                            afirm = False
                else:
                    afirm = False
            
            if afirm == True and not len(jogador["nome"]) == 0:
                try:
                    jogador["nome"] = int(jogador["nome"])
                    print("[bold red]Só pode letras![/]\n")
                except:
                    nome_comp = jogador["nome"].split(" ")
                        
                    for i,n in enumerate(nome_comp):
                        if len(n) == 0:
                            afirm = False
                    print(len(nome_comp))
                    
                    if afirm == True:
                        if len(nome_comp) < 2:
                            while True:
                                afirm = True
                                try:
                                    composto = input(f'Digite um sobrenome para {jogador["nome"]}: ')
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    break
                                else:
                                    if len(composto) == 0:
                                        print("[bold red]Valor invalido![/]")
                                    else:
                                        sep = composto.split(" ")

                                        for i,n in enumerate(sep):
                                            if len(n) == 0:
                                                afirm = False

                                        if afirm == True and len(sep) <= 2:
                                            try:
                                                composto = int(composto)
                                                print("\n[bold red]Apenas letras![/]\n")
                                            except (ValueError,TypeError):
                                                break
                                        else:
                                            print("[bold red]Valor invalido![/]")
                                                        
                                                    
                            if proximo == True:
                                nome_comp.append(composto)
                                nome_comp = nome_comp[0] + ' ' + nome_comp[1]   
                                jogador['nome'] = nome_comp.lower().capitalize()
                                break
                            else:
                                break

                        elif len(nome_comp) >= 3:
                            print("[bold red]É permitido apenas três nomes e no minimo dois nomes![/]\n")
                        else:
                            break
                    else:
                        print("[bold red]Valor invalido![/]")
            else:
                print("[bold red]Valor invalido![/]")


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
            afirm = True
            try:
                jogador['nacionalidade'] = input("Digite a nacionalidae do jogador: ")
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar[/]\n")
                proximo = False
                break
            else:
                comp = jogador["nacionalidade"].split(" ")
                
                for i,n in enumerate(comp):
                    try:
                        int(n)
                    except:
                        for m in n:
                            try:
                                int(m)
                            except:
                                pass
                            else:
                                afirm = False
                    else:
                        afirm = False

                if len(jogador['nacionalidade']) == 0 and afirm == False:
                    print("[bold red]Digite uma nacionalidade valida![/]\n")
                else:
                    comp = jogador['nacionalidade'].split(" ")

                    for i,n in enumerate(comp):
                        if len(n) == 0:
                            afirm = False
                    if afirm == True:
                        try:
                            jogador['nacionalidade'] = int(jogador['nacionalidade'])
                            print("[bold red]Digite uma nacionalidade valida![/]\n")
                        except:
                            break
                    else:
                        print("[bold red]Digite uma nacionalidade valida![/]\n")
                        
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
