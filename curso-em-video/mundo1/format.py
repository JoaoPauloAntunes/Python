n1 = int(input('n1: '))
n2 = int(input('n2: '))

soma = n1 + n2
print('a soma de {} e {} é {}'.format(n1, n2, soma))

sub = n1 - n2
print('a subtração de {} e {} é {}'.format(n1, n2, sub))

mult = n1 * n2
print('a multiplicação de {} e {} é {}'.format(n1, n2, mult))

div = n1 / n2
# restringe a resposta a duas casas decimais  
print('a divisão de {} e {} é {:.2f}'.format(n1, n2, div))

divInt = n1 // n2
print('a dvisão inteira de {} e {} é {}'.format(n1, n2, divInt))

pot = n1 ** n2
print('a potência de {} e {} é {}'.format(n1, n2, pot))

resto = n1 % n2
print('o resto de divisão de {} e {} é {}'.format(n1, n2, resto))

input()
