# um litro de tinta pinta uma área de 2m²
larg = float(input('Largula: ')) 
alt = float(input('Altura: '))
area = larg * alt
print('área: {} m²'.format(area))
print('Quantidade de tinta necessária para pintar a parede: {} L'.format(area / 2))
input()