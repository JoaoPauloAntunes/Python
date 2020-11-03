produto1 = float(input('1° Produto: '))
produto2 = float(input('2° Produto: '))
produto3 = float(input('3° Produto: '))

print('')

if produto1 < produto2:
    if produto1 < produto3:
        print('comprar: 1° Produto')
    else:
        print('comprar: 3° Produto')
elif produto2 < produto3:
    print('comprar: 2° Produto')
else:
    print('comprar: 3° Produto')