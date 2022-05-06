from função_cadastrar import cadastrar
from função_comprar import comprar
from função_visualizar import visualizar
from rich import print

def menu():
    opcao = '[1][bold green]Cadastrar jogador[/] \n[2][bold yellow]Comprar jogador[/]\n[3][bold blue]Visualizar os times[/]'
    print(opcao)

while True:
    print('-'*20)
    menu()
    print('-'*20)
    try:
        opcao = int(input("Digite um valor(Apenas: 1 ou 2 ou 3): "))
    except (ValueError,TypeError):
        print('[bold red]Apenas valores númericos![/]')
    except KeyboardInterrupt:
        print("\n[#ff6f00]Até mais.[/]")
        break
    else:
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            comprar()
        elif opcao == 3:
            visualizar()
        else:
            print("-"*20)
            print("\n[bold red]Valor invalido![/]\n")