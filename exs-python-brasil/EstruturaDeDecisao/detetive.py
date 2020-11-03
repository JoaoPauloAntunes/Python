telefonouParaVitima = bool(input('Telefonou para a vítima (S/N)? ') == 'S')
esteveLocalCrime = bool(input('Esteve no local do crime (S/N)? ') == 'S')
moraPertoVitima = bool(input('Mora perto da vítima (S/N)? ') == 'S')
deviaParaVitima = bool(input('Devia para a vítima (S/N)? ') == 'S')
trabalhouComVitima = bool(input('Já trabalhou com a vítima (S/N)? ') == 'S')

pontos = 0
if telefonouParaVitima:
    pontos += 1
if esteveLocalCrime:
    pontos += 1
if moraPertoVitima:
    pontos += 1
if deviaParaVitima:
    pontos += 1
if trabalhouComVitima:
    pontos += 1

print('Classificação: ', end='')
if pontos == 2:
    print('Suspeita')
elif pontos == 3 or pontos == 4:
    print('Cúmplice')
elif pontos == 5:
    print('Assassino')
else:
    print('Inocente')
