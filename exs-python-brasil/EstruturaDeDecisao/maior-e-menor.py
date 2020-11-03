num1 = float(input('1° Número: '))
num2 = float(input('2° Número: '))
num3 = float(input('3° Número: '))

print('')

if num1 > num2:
    if num1 > num3:
        print('1° Número é maior')
    else:
        print('3° Número é maior')
elif num2 > num3:
    print('2° Número é maior')
else:
    print('3° Número é maior')

if num1 < num2:
    if num1 < num3:
        print('1° Número é menor')
    else:
        print('3° Número é menor')
elif num2 < num3:
    print('2° Número é menor')
else:
    print('3° Número é menor')