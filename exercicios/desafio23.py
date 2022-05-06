numeri = int(input("Digite um numero de 0 a 9999\n"))

while numeri < 0 or numeri > 9999:
    numeri = int(input("Numeor invalido. Digite novamente\n"))

unidade = numeri % 10   
print("Unidade:",unidade)
numero = (numeri - unidade)/10
dezena = (numero)%10
print("Dezena:",dezena)
numero = (numero - dezena)/10
centena = (numero)%10
print("Centena:",centena)
milhar = (numero - centena)/10
print("Milhar:",milhar)