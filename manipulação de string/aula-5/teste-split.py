'''
p = "nome"
print(p.split())
print(p.split(" "))

p = "n o m e"
print(p.split())
print(p.split(" "))
'''

lista = "Milk, Chicken, Bread, Butter"
#maxsplit 1:
print(lista.split(',',0))
#maxsplit 2:
print(lista.split(',',1))
#maxsplit 3:
print(lista.split(',',2))
#maxsplit 4:
print(lista.split(',',5))