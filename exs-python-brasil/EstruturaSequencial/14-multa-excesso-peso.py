peso = float(input('peso de peixes (Kg): '))
MAX_PESO_PEIXES = 50
VALOR_MULTA_KILO_EXCEDENTE = 4

if peso > MAX_PESO_PEIXES:
    excesso = peso - MAX_PESO_PEIXES
    multa = excesso*VALOR_MULTA_KILO_EXCEDENTE
    print(f'O peso de peixes excedeu em {excesso} Kg e a valor da multa ficou: R$ {multa}')
else:
    print(f'O peso de peixes está abaixo do máximo ({MAX_PESO_PEIXES})')