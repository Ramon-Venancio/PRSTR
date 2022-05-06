from armazenamento import A,B,a_carteira,b_carteira
from rich.table import Table
from rich.console import Console
from rich import print


def visualizar():
    print("\n")

    tablet = Table(title="Carteira dos times")
    tableA = Table(title="Jogadores do time A")
    tableB = Table(title="Jogadores do time B")
    console = Console()

    tablet.add_column("[bold green]Times[/]")
    tablet.add_column("[bold yellow]Carteira do time[/]")
    if len(a_carteira) == 0:
        tablet.add_row("[bold green]A[/]","[bold yellow]0[/]")
    else:
        tablet.add_row("[bold green]A[/]",f'[bold yellow]{str(a_carteira[0])}[/]')
    if len(b_carteira) == 0:
        tablet.add_row("[bold green]B[/]","[bold yellow]0[/]")
    else:
        tablet.add_row("[bold green]B[/]",f'[bold yellow]{str(b_carteira[0])}[/]')

    tableA.add_column("[bold blue]Jogadores[/]")
    tableA.add_column("[bold #ff6f00]Idade[/]")
    tableA.add_column("[bold #A62A2A]Nacionalidade[/]")
    tableA.add_column("[bold green]Gols[/]")
    tableA.add_column("[bold yellow]Salario[/]")
    for k,i in enumerate(A):
        tableA.add_row(f'[bold blue]{i["nome"]}[/]',f'[bold #ff6f00]{str(i["idade"])}[/]',f'[bold #A62A2A]{i["nacionalidade"]}[/]',f'[bold green]{str(i["gols"])}[/]',f'[bold yellow]{str(i["salario"])}[/]')

    tableB.add_column("[bold blue]Jogadores[/]")
    tableB.add_column("[bold #ff6f00]Idade[/]")
    tableB.add_column("[bold #A62A2A]Nacionalidade[/]")
    tableB.add_column("[bold green]Gols[/]")
    tableB.add_column("[bold yellow]Salario[/]")
    for k,i in enumerate(B):
        tableB.add_row(f'[bold blue]{i["nome"]}[/]',f'[bold #ff6f00]{str(i["idade"])}[/]',f'[bold #A62A2A]{i["nacionalidade"]}[/]',f'[bold green]{str(i["gols"])}[/]',f'[bold yellow]{str(i["salario"])}[/]')
    
    console.print(tablet)
    console.print(tableA)
    console.print(tableB)