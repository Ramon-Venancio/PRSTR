jogador = {} 
A = []
B = []
a_carteira = 0
b_carteira = 0

def menu():
    opcao = '[1]Cadastrar jogador \n[2]Comprar jogador\n[3]Visualizar os times'
    print(opcao)

def cadastrar():
    global a_carteira
    global b_carteira
    print('-'*20)
    jogador['nome'] = input('Digite o nome do jogador: ').lower().capitalize()
    nome_comp = jogador['nome'].split()
    if len(nome_comp) < 2:
        composto = input(f'Digite um sobrenome para {jogador["nome"]}: ')
        nome_comp.append(composto)
        nome_comp = nome_comp[0] + ' ' + nome_comp[1] 
        jogador['nome'] = nome_comp.lower().capitalize()

    nome_comp = jogador['nome'].split()

    if len(nome_comp) > 3:
        print('É permitido apenas três nomes e no minimo dois nomes!!!')
        while len(nome_comp) > 3 or len(nome_comp) < 2:
            jogador['nome'] = input('Digite o nome do jogador: ').lower().capitalize()
            nome_comp = jogador['nome'].split()
    else:
        pass

    jogador['idade'] = ''
    while jogador['idade'] == '':
        try:
            jogador['idade'] = int(input('Digite a idade do jogador: '))
        except:
            print('Valor invalido! Apenas palavras!!')

    jogador['nacionalidade'] = ''
    while jogador['nacionalidade'] == '':
        jogador['nacionalidade'] = str(input('Digite a nacionalidae do jogador: '))
        while True:
            try:
                jogador['nacionalidade'] = int(jogador['nacionalidade'])
                jogador['nacionalidade'] = input('Digite a nacionalidade valida: ')
            except:
                jogador['nacionalidade'] = jogador['nacionalidade']
                break

    jogador['gols'] = ''

    while jogador['gols'] == '':
        try:
            jogador['gols'] = int(input('Digite a quantidade de gols na ultima temporada: '))
        except:
            print('Valor invalido! Apenas valores númericos')

    jogador['salario'] = ''
    while jogador['salario'] == '':
        try:
            jogador['salario'] = int(input('Digite o salario do jogador: '))
        except:
            print('Valor invalido! Apenas valores númericos')

    time = input('Qual time o jogador pertence(A/B)?: ').upper()
    while time != 'A' and time != 'B':
        time = input('Qual time o jogador pertence(Escolha entre o time A ou B)?: ').upper()
    if time == 'A':
        a_carteira = a_carteira + jogador['salario']
        A.append(jogador.copy())
    elif time == 'B':
        b_carteira = b_carteira + jogador['salario']
        B.append(jogador.copy())
    else:
        print('Valor invalido')

        
def comprar():
    global a_carteira
    global b_carteira
    time = input('Qual o seu time?(A/B): ').upper()
    while time != 'A' and time != 'B':
        time = input('Qual o seu time?(Apenas time A ou B)?: ').upper()
    if time == 'A':
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
                for i,dados in enumerate(B) :
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
                    for i,dados in enumerate(B):
                        nome = dados['nome']
                        transferencia = i
                        salario = dados['salario']
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
        elif escolha == 'GOLS':
            continuar = 1
            while continuar == 1:
                gol = ''
                while gol == '':
                    try:
                        gol = int(input('Digite a quantidade de gols minima: '))
                    except:
                        print('Valor invalido! Apenas valores númericos')
                for i,dados in enumerate(B) :
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
def visualizar():
    print('-'*20)
    print('Jogadores do time A:')
    print(A)
    print(F'Carteira de a {a_carteira}')
    print('-'*20)
    print('Jogadores do time B: ')
    print(B)
    print(f'Carteira de b {b_carteira}')
    
while True:
    print('-'*20)
    menu()
    print('-'*20)
    opcao = ''
    while opcao == '':
        try:
            opcao = int(input('Digite um valor(Apenas: 1 ou 2 ou 3): '))
           
        except:
            print('Apenas valores númericos')
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        comprar()
    elif opcao == 3:
        visualizar()
    else:
        print('Valor invalido')