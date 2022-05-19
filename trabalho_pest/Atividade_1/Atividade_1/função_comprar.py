from armazenamento import jogador,A,B,a_carteira,b_carteira
from rich import print

def comprar():
    global a_carteira
    global b_carteira
    proximo = True
    jogadores = []
    try:
        time = input('Qual o seu time?(A/B): ').upper()
    except KeyboardInterrupt:
        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
    else:
        while time != 'A' and time != 'B':
            try:
                time = input('Qual o seu time?(Apenas time A ou B)?: ').upper()
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                break

    if time == 'A':
        while proximo == True:
            jogadores.clear()
            afirm = True
            try:
                escolha = input('Digite o que você quer procurar(Idade/Gols/Salario): ').upper()
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                break

            if escolha == 'IDADE':
                jogadores.clear()
                try:
                    minima = int(input('Digite idade minima: '))
                except KeyboardInterrupt:
                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                    proximo = False
                    break
                except (ValueError,TypeError):
                    print("[bold red]Valor invalido! Apenas valores númericos[/]")
                else:
                    try:
                        maxima = int(input('Digite idade maxima: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except (ValueError,TypeError):
                        print('\n[bold red]Valor invalido! Apenas valores númericos[/]\n')
                    else:
                        for i,dados in enumerate(B):
                            if dados['idade'] >= minima and dados['idade'] <= maxima:
                                print("-"*20)
                                print(f'[bold blue]Nome:[/] {dados["nome"]}\n[bold #ff6f00]Idade:[/] {dados["idade"]}\n[bold yellow]Sálario:[/] {dados["salario"]}')
                                print(f'{"-"*20}\n')
                                jogadores.append(dados)

                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com essa idade.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas valores númericos![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if a_carteira[0] >= salario:
                                                        A.append(dados)
                                                        del B[transferencia]
                                                        a_carteira[0] = a_carteira[0] - salario
                                                        b_carteira[0] = b_carteira[0] + salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                print("[bold red]Jogador não encontrado[/]\n")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                            try:
                                print('Você quer:\n[1][bold blue]Pesquisar novamente?[/]\nou\n[2][bold #ff6f00]Desistir?[/]')
                                continuar = int(input(": "))
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            except (ValueError,TypeError):
                                print("[bold red]Digite apenas valores númericos![/]")
                            else:
                                if continuar == 1:
                                    pass
                                elif continuar == 2:
                                    proximo = False
                                    break

            elif escolha == 'GOLS':
                while afirm == True:
                    afirm = True
                    try:
                        gol = int(input('Digite a quantidade de gols minima: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except(ValueError,TypeError):
                        print('Valor invalido! Apenas valores númericos')
                    else:
                        for i,dados in enumerate(B):
                            if dados['gols'] >= gol:
                                print("-"*20)
                                print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold #ff6f00]Gols: {dados["gols"]}[/]\nSálario: {dados["salario"]}')
                                print(f'{"-"*20}\n')
                                jogadores.append(dados)
                            
                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com essa quantidade minima de gols.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas números![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if a_carteira[0] >= salario:
                                                        A.append(dados)
                                                        del B[transferencia]
                                                        a_carteira[0] = a_carteira[0] - salario
                                                        b_carteira[0] = b_carteira[0] + salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                    print("[bold red]Jogador não encontrado[/]")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                            try:
                                print('Você quer:\n[1][bold blue]Pesquisar novamente?[/]\nou\n[2][bold #ff6f00]Desistir?[/]')
                                continuar = int(input(": "))
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            except (ValueError,TypeError):
                                print("[bold red]Digite apenas valores númericos![/]")
                            else:
                                if continuar == 1:
                                    pass
                                elif continuar == 2:
                                    proximo = False
                                    break
                            
            elif escolha == 'SALARIO':
                while afirm == True:
                    try:
                        salario_desejavel = int(input('Digite o salario: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except (ValueError,TypeError):
                        print('Valor invalido! Apenas valores númericos')
                    else:
                        for i,dados in enumerate(B):
                            if dados["salario"] <= salario_desejavel:
                                print('-'*20)
                                print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold yellow]Salario: {dados["salario"]}[/]')
                                print('-'*20)
                                jogadores.append(dados)
                        
                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com esse sálario.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas números![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if a_carteira[0] >= salario:
                                                        B.append(dados)
                                                        del A[transferencia]
                                                        a_carteira[0] = a_carteira[0] - salario
                                                        b_carteira[0] = b_carteira[0] + salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                    print("[bold red]Jogador não encontrado[/]\n")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                            try:
                                print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\nou\n[2][bold #ff6f00]Desistir[/]')
                                continuar = int(input(": "))
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            except (ValueError,TypeError):
                                print("[bold red]Digite apenas valores númericos![/]")
                            else:
                                if continuar == 1:
                                    pass
                                elif continuar == 2:
                                    proximo = False
                                    break
            else:
                print("[bold red]Digite de acordo com as sugestões![/]")
                                
    elif time == 'B':
       while proximo == True:
            jogadores.clear()
            afirm = True
            try:
                escolha = input('Digite o que você quer procurar(Idade/Gols/Salario): ').upper()
            except KeyboardInterrupt:
                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                break

            if escolha == 'IDADE':
                jogadores.clear()
                try:
                    minima = int(input('Digite idade minima: '))
                except KeyboardInterrupt:
                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                    proximo = False
                    break
                except (ValueError,TypeError):
                    print("[bold red]Valor invalido! Apenas valores númericos[/]")
                else:
                    try:
                        maxima = int(input('Digite idade maxima: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except (ValueError,TypeError):
                        print('\n[bold red]Valor invalido! Apenas valores númericos[/]\n')
                    else:
                        for i,dados in enumerate(A):
                            if dados['idade'] >= minima and dados['idade'] <= maxima:
                                print("-"*20)
                                print(f'[bold blue]Nome:[/] {dados["nome"]}\n[bold #ff6f00]Idade:[/] {dados["idade"]}\n[bold yellow]Sálario:[/] {dados["salario"]}')
                                print(f'{"-"*20}\n')
                                jogadores.append(dados)

                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com essa idade.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas valores númericos![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if a_carteira[0] >= salario:
                                                        B.append(dados)
                                                        del A[transferencia]
                                                        a_carteira[0] = a_carteira[0] + salario
                                                        b_carteira[0] = b_carteira[0] - salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        print(afirm)
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                print("[bold red]Jogador não encontrado[/]\n")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                                    try:
                                        print('Você quer:\n[1][bold blue]Pesquisar novamente?[/]\nou\n[2][bold #ff6f00]Desistir?[/]')
                                        continuar = int(input(": "))
                                    except KeyboardInterrupt:
                                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                        proximo = False
                                        break
                                    except (ValueError,TypeError):
                                        print("[bold red]Digite apenas valores númericos![/]")
                                    else:
                                        if continuar == 1:
                                            pass
                                        elif continuar == 2:
                                            proximo = False
                                            break

            elif escolha == 'GOLS':
                while afirm == True:
                    afirm = True
                    try:
                        gol = int(input('Digite a quantidade de gols minima: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except(ValueError,TypeError):
                        print('Valor invalido! Apenas valores númericos')
                    else:
                        for i,dados in enumerate(A):
                            if dados['gols'] >= gol:
                                print("-"*20)
                                print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold #ff6f00]Gols: {dados["gols"]}[/]\nSálario: {dados["salario"]}')
                                print(f'{"-"*20}\n')
                                jogadores.append(dados)
                            
                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com essa quantidade minima de gols.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas números![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if b_carteira[0] >= salario:
                                                        B.append(dados)
                                                        del A[transferencia]
                                                        a_carteira[0] = a_carteira[0] + salario
                                                        b_carteira[0] = b_carteira[0] - salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                    print("[bold red]Jogador não encontrado[/]")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                            try:
                                print('Você quer:\n[1][bold blue]Pesquisar novamente?[/]\nou\n[2][bold #ff6f00]Desistir?[/]')
                                continuar = int(input(": "))
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            except (ValueError,TypeError):
                                print("[bold red]Digite apenas valores númericos![/]")
                            else:
                                if continuar == 1:
                                    pass
                                elif continuar == 2:
                                    proximo = False
                                    break
                            
            elif escolha == 'SALARIO':
                while afirm == True:
                    try:
                        salario_desejavel = int(input('Digite o salario: '))
                    except KeyboardInterrupt:
                        print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                        proximo = False
                        break
                    except (ValueError,TypeError):
                        print('Valor invalido! Apenas valores númericos')
                    else:
                        for i,dados in enumerate(A):
                            if dados["salario"] <= salario_desejavel:
                                print('-'*20)
                                print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold yellow]Salario: {dados["salario"]}[/]')
                                print('-'*20)
                                jogadores.append(dados)
                        
                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com esse sálario.[/]\n")
                        else:
                            while True:
                                try:
                                    print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\n[2][bold #ff6f00]Desistir[/]\n[3][bold yellow]Comprar[/]')
                                    continuar = int(input(": "))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    proximo = False
                                    afirm = False
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas números![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        proximo = False
                                        break
                                    elif continuar == 1:
                                        afirm = False
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                            proximo = False
                                            afirm = False
                                            break
                                        else:
                                            for i,dados in enumerate(jogadores):
                                                transferencia = i
                                                salario = dados['salario']
                                                if dados['nome'] == jogador:
                                                    if a_carteira[0] >= salario:
                                                        A.append(dados)
                                                        del B[transferencia]
                                                        a_carteira[0] = a_carteira[0] + salario
                                                        b_carteira[0] = b_carteira[0] - salario
                                                        print(f'Valor da carteira B foi atualizado: {b_carteira[0]}')
                                                        print(f'Valor da carteira A foi atualizado: {a_carteira[0]}')
                                                        break
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    afirm = False
                                            if afirm == False:
                                                    print("[bold red]Jogador não encontrado[/]\n")
                                            else:
                                                break
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                        if afirm == True:
                            try:
                                print('Você quer:\n[1][bold blue]Pesquisar novamente[/]\nou\n[2][bold #ff6f00]Desistir[/]')
                                continuar = int(input(": "))
                            except KeyboardInterrupt:
                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                proximo = False
                                break
                            except (ValueError,TypeError):
                                print("[bold red]Digite apenas valores númericos![/]")
                            else:
                                if continuar == 1:
                                    pass
                                elif continuar == 2:
                                    proximo = False
                                    break
            else:
                print("[bold red]Digite de acordo com as sugestões![/]")