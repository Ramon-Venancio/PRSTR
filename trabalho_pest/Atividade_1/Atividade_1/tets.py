afirm = True
n = input("Algo: ")

p = n.split(" ")

print(p)
print(len(p[0]))

for i,n in enumerate(p):
    if len(n) == 0:
        afirm = False

if afirm == False:
    print("batata")
else:
    print("deu certo.")