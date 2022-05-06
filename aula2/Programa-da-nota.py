#Programa da nota:
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

while (n1 < 0 or n1 > 10) or (n2 < 0 or n2 > 10):
    if n1 < 0 or n1 > 10:
        n1 = float(input("Digite novamente a primeira nota: "))
    if n2 < 0 or n2 > 10:
        n2 = float(input("Digite novamente a segunda nota: "))

media = (n1 + n2) / 2

n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

while (n3 < 0 or n3 > 10) or (n4 < 0 or n4 > 10):
    if n3 < 0 or n3 > 10:
        n3 = float(input("Digite novamente a terceira nota: "))
    if n4 < 0 or n4 > 10:
        n4 = float(input("Digite novamente a quarta nota: "))

media2 = (n3 + n4) / 2
media_g = (media + media2) / 2

if media_g > 7:
    print("Você passou.")
elif media_g > 3:
    print("Você ficou de recuperação.")
    
    n_pf = float(input("Digite a nota da pova final: "))
    media_final = (media + n_pf) / 2
    
    if media_final > 5:
        print("Você passou.")
    else:
        print("Você reprovou")
else:
    print("Você reprovou.")