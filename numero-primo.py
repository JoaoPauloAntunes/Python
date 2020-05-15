n = int(input('Digite um número: '))

primo = True
if n <= 1 or (n > 2 and n%2 == 0):
    primo = False
else:
    for i in range(3, n, 2):
        if n%i == 0:
            primo = False
            break
if primo:
    print('É primo!')
else:
    print('Não é primo!')