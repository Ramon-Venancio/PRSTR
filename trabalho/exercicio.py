n = int(input('Digite um numero: '))
mult = 0 
for count in range(2,n):
    if(n % count == 0):
        print('Multiplo de {:^.10}'.format(count))
        mult += 1 
if (mult ==0):
    print('É primo') 