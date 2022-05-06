#O lstrip remove todos os espaços em branco do lado esquerdo dastring.
#O rsstrip remove todos os espaços em branco do lado direito da string.
#O strip remove todos os espaços em branco da string.
#Sintaxe: str.{l ou r}strip([chars])
#Exemplos:
nome = "--------geetsforgeets---------"

print(nome.strip('-'))
print(nome.lstrip('-'))
print(nome.rstrip('-'))