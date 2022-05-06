#O ljust Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se necessário.
#Sintaxe: str.ljust(width[,fillchar])
#Ps.: Width - Este é o tamanho da string no total após o preenchimento. Ele considera o tamnho atual d string + preenchimento.
# Fillchar - Esse é o caractere de preenchimento, o padrão é um espaço.
#Exemplos:
nome = "cat"
width = 5
fillchar = "*"
i = 1

print(nome.ljust(width, fillchar))

str = "Poke"
print(str.ljust(50, '0'))

txt = "mon"
x = txt.ljust(20, '0')
print(x,'\n')

#O rjust Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se necessário.
#Sintaxe: str.rjust(width[,fillchar])
#Exemplos:
nome = "cat"
width = 5
fillchar = "*"
i = 1

print(nome.rjust(width, fillchar))

str = "Poke"
print(str.rjust(50, '0'))

txt = "mon"
x = txt.rjust(20, '0')
print(x,'\n')
#O center Ajusta a string para um tamanho mínimo, acrescentando espaços à direita se necessário.
#Sintaxe: str.center(len,fillchar)
#P.s.: len - Este é o tamanho da string no total após o preenchimento. Ele considera o tamnho atual da string + preenchimento.
#Exemplos:
nome = "cat"
len = 5
fillchar = "*"
i = 1

print(nome.center(len, fillchar))

str = "Poke"
print(str.center(50, '0'))

txt = "mon"
x = txt.center(20, '0')
print(x)