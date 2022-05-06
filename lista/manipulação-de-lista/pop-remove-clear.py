#O "pop" remove e mostra o elemento removido.
#Sintaxe: var.pop(indice)
#O "remove" remove um lemento pelo nome dele.
#Sintaxe: var.remove(nome)
#O clear apaga toda a lista.
#Sintaxe: var.clear()
#Exs.:

lista = ["p","r","s","t","u","v"]
lista.remove("p")
print(lista)

print(lista.pop(1))
print(lista)

print(lista.pop())
print(lista)

print(lista.clear())
print(lista)