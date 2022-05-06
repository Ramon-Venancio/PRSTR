#O operador [x:x] de fatiamento separa a lista. x = numero de fatiamento.
#Exemplos:
t = ["a","b","c","d","e","f"]

#Sem omitir nada, vai separa uma parte da lista:
f = t[1:3] #O primeiro indice vai tirar a letra "a" e o segundo indice vai tirar as letras "d,e,f".
print(f, "\n")

#Se omitimos o primeiro indice, a fatia começara no início:
f = t[:4]
print(f, "\n")

#Se omitimos o segundo indice, a fatia começara do final:
f = t[3:]
print(f,"\n")

#Se omitimos ambos os indices, a fatia será uma copia da lista:
f = t[:]
print(f,"\n")

#Modificando a lista:
t[1:3] = ["x","y"]
print(t)