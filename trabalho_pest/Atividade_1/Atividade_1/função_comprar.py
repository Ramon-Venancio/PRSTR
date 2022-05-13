from armazenamento import jogador,A,B,a_carteira,b_carteira
from rich import print

def comprar():
    global a_carteira
    global b_carteira
    proximo = True
    jogadores = []
    time = input('Qual o seu time?(A/B): ').upper()
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
                while afirm == True:
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
                                    print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold #ff6f00]Idade: {dados["idade"]}[/]')
                                    print(f'{"-"*20}\n')
                                    jogadores.append(dados)

                            if len(jogadores) == 0:
                                print("[bold red]Não exite um jogador com essa idade.[/]\n")
                            else:
                                while True:
                                    try:
                                        continuar = int(input('Você quer:\n[bold blue][1]Pesquisar novamente\n[bold #ff6f00][2]Desistir[/]\n[bold yellow][3]Comprar[/]'))
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
                                            break
                                        elif continuar == 1:
                                            break
                                        elif continuar == 3:
                                            try:
                                                jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                            except KeyboardInterrupt:
                                                print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
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
                                                        print('Jogador não encontrado')
                                        else:
                                            print("[bold red]Digite de acordo com as sugestões![/]")
                                    
                                if afirm == True:
                                    try:
                                        continuar = int(input('Você quer:\n[bold blue][1]Pesquisar novamente\nou\n[bold #ff6f00][2]Desistir[/]\n: '))
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
                                print(f'[bold blue]Nome: {dados["nome"]}[/]\n[bold #ff6f00]Gols: {dados["gols"]}[/]')
                                print(f'{"-"*20}\n')
                                jogadores.append(dados)
                            
                        if len(jogadores) == 0:
                            print("[bold red]Não exite um jogador com essa quantidade minima de gols.[/]\n")
                        else:
                            while True:
                                try:
                                    continuar = int(input('Você quer:\n[bold green][1]Pesquisar novamente[/]\n[bold #ff6f00][2]Desistir[/]\n[bold yellow][3]Comprar[/]\n: '))
                                except KeyboardInterrupt:
                                    print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
                                    break
                                except (ValueError,TypeError):
                                    print("[bold red]Digite apenas números![/]")
                                else:
                                    if continuar == 2:
                                        afirm = False
                                        break
                                    elif continuar == 1:
                                        break
                                    elif continuar == 3:
                                        try:
                                            jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                                        except KeyboardInterrupt:
                                            print("\n[#ff6f00]O usuário não quis mais continuar.[/]\n")
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
                                                    else:
                                                        print('Você não tem saldo suficiente!')
                                                else:
                                                    print('Jogador não encontrado')
                                    else:
                                        print("[bold red]Digite de acordo com as sugestões![/]")

                            if afirm == True:
                                    try:
                                        continuar = int(input('Você quer:\n[bold blue][1]Pesquisar novamente\nou\n[bold #ff6f00][2]Desistir[/]\n: '))
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
                                            break
                                        else:
                                            print("[bold red]Digite de acordo com as sugestões![/]")
                            

            elif escolha == 'SALARIO':
                continuar = 1
                while continuar == 1:
                    salario_desejavel = ''
                    while salario_desejavel == '':
                        try:
                            salario_desejavel = int(input('Digite o salario: '))
                        except:
                            print('Valor invalido! Apenas valores númericos')
                    for i,dados in enumerate(B):
                        jogador_completo = dados
                        posicao = i
                        salario = dados['salario']
                        nome = dados['nome']
                        gols = dados['gols']
                        if salario <= salario_desejavel:
                            print('-'*20)
                            print(f'Nome: {nome}\nSalario: {salario}')
                    print('-'*20)
                    continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                    while continuar != 1 and continuar != 2 and continuar != 3:
                        continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                    if continuar == 3:
                        jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                        for i,dados in enumerate(B):
                            nome = dados['nome']
                            transferencia = i
                            if nome == jogador:
                                if a_carteira >= salario:
                                    A.append(dados)
                                    del B[transferencia]
                                    a_carteira = a_carteira - salario
                                    b_carteira = b_carteira + salario
                                    print(f'Valor da carteira B foi atualizado: {b_carteira}')
                                    print(f'Valor da carteira A foi atualizado: {a_carteira}')
                                else:
                                    print('Você não tem saldo suficiente!')
                            else:
                                print('Jogador não encontrado')
                                
    elif time == 'B':
        escolha = input('Digite o que você quer procurar(Idade/Gols/Salario): ').upper()
        while escolha != 'IDADE' and escolha != 'GOLS' and escolha != 'SALARIO':
            print('Informação não encontrada')
            escolha = input('Digite o que você quer procurar(Idade/Gols/Salario): ').upper()
        if escolha == 'IDADE':
            continuar = 1
            while continuar == 1:
                minima = ''
                while minima == '':
                    try:
                        minima = int(input('Digite idade minima: '))
                    except:
                        print('Valor invalido! Apenas valores númericos')
                maxima = ''
                while maxima == '':
                    try:
                        maxima = int(input('Digite idade maxima: '))
                    except:
                        print('Valor invalido! Apenas valores númericos')
                for i,dados in enumerate(A):
                    jogador_completo = dados
                    posicao = i
                    salario = dados['salario']
                    nome = dados['nome']
                    gols = dados['gols']
                    idade = dados['idade']
                    if idade >= minima and idade <= maxima:
                        print('-'*20)
                        print(f'Nome: {nome}\nIdade: {idade}\n')
                print('-'*20)
                continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                while continuar != 1 and continuar != 2 and continuar != 3:
                    continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                if continuar == 3:
                    jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                    for i,dados in enumerate(A):
                        nome = dados['nome']
                        transferencia = i
                        if nome == jogador:
                            if b_carteira >= salario:
                                B.append(dados)
                                del A[transferencia]
                                a_carteira = a_carteira + salario
                                b_carteira = b_carteira - salario
                                print(f'Valor da carteira B foi atualizado: {b_carteira}')
                                print(f'Valor da carteira A foi atualizado: {a_carteira}')
                            else:
                                print('Você não tem saldo suficiente!')
                        else:
                            print('Jogador não encontrado')
                    
        elif escolha == 'GOLS':
            continuar = 1
            while continuar == 1:
                gol = ''
                while gol == '':
                    try:
                        gol = int(input('Digite a quantidade de gols minima: '))
                    except:
                        print('Valor invalido! Apenas valores númericos')
                for i,dados in enumerate(A):
                    jogador_completo = dados
                    posicao = i
                    salario = dados['salario']
                    nome = dados['nome']
                    gols = dados['gols']
                    if gols >= gol:
                        print('-'*20)
                        print(f'Nome: {nome}\nGols: {gols}')
                print('-'*20)
                continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                while continuar != 1 and continuar != 2 and continuar != 3:
                    continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                if continuar == 3:
                    jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                    for i,dados in enumerate(A):
                        nome = dados['nome']
                        transferencia = i
                        if nome == jogador:
                            if b_carteira >= salario:
                                B.append(dados)
                                del A[transferencia]
                                a_carteira = a_carteira + salario
                                b_carteira = b_carteira - salario
                                print(f'Valor da carteira B foi atualizado: {b_carteira}')
                                print(f'Valor da carteira A foi atualizado: {a_carteira}')
                            else:
                                print('Você não tem saldo suficiente!')
                        else:
                            print('Jogador não encontrado')

        elif escolha == 'SALARIO':
            continuar = 1
            while continuar == 1:
                salario_desejavel = ''
                while salario_desejavel == '':
                    try:
                        salario_desejavel = int(input('Digite o salario: '))
                    except:
                        print('Valor invalido! Apenas valores númericos')
                for i,dados in enumerate(A):
                    jogador_completo = dados
                    posicao = i
                    salario = dados['salario']
                    nome = dados['nome']
                    gols = dados['gols']
                    if salario <= salario_desejavel:
                        print('-'*20)
                        print(f'Nome: {nome}\nSalario: {salario}')
                print('-'*20)
                continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                while continuar != 1 and continuar != 2 and continuar != 3:
                    continuar = int(input('[1]Pesquisar novamente\n[2]Desistir\n[3]Comprar\nDigite um valor:'))
                if continuar == 3:
                    jogador = input('Qual jogador você se interessou?: ').lower().capitalize()
                    for i,dados in enumerate(A):
                        nome = dados['nome']
                        transferencia = i
                        if nome == jogador:
                            if b_carteira >= salario:
                                B.append(dados)
                                del A[transferencia]
                                a_carteira = a_carteira + salario
                                b_carteira = b_carteira - salario
                                print(f'Valor da carteira B foi atualizado: {b_carteira}')
                                print(f'Valor da carteira A foi atualizado: {a_carteira}')
                            else:
                                print('Você não tem saldo suficiente!')
                        else:
                            print('Jogador não encontrado')
        else:
            pass