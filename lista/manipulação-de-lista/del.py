#O del deleta algo na lista.
#Sintaxe: del var[indice].
#Exs.:
lista = ["a","b","c","d","e","f","g","h"]

del lista[2]
print(lista)

del lista[1:5]
print(lista)

del lista[-2]
print(lista)

del lista[2:-4]
print(lista)

del lista[4:-4]
print(lista)

del lista[-5:-4]
print(lista)
  
del lista