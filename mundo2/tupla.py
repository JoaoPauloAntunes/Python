from random import randint

"""
tupla, def, import randint

PEDRA x PAPEL : PAPEL
PEDRA x TESOURA : PEDRA

PAPEL x PEDRA : PAPEL
PAPEL x TESOURA : TESOURA

TESOURA x PEDRA : PEDRA
TESOURA x PAPEL : TESOURA
"""

def msgVence(op, jogador):
	print(op + "\n" + jogador + " vence!")

lis = ('PEDRA', 'PAPEL', 'TESOURA')

print('''Escolha
[0]: PEDRA
[1]: PAPEL
[2]: TESOURA''')
# print()
op1 = int(input('Escolher: ')) % 3
jogador1 = lis[op1]

op2 = randint(0, 2)
if op1 == op2:
	op2 += 1
	op2 %= 3

computador = lis[op2]

print('\n{} x {} : '.format(jogador1, computador), end='')

if computador ==  'PEDRA':
	if jogador1 == 'PAPEL':
		msgVence("PAPEL", "jogador1")
	else:
		msgVence("PEDRA", "computador")
elif computador == "PAPEL":
	if jogador1 == 'PEDRA':
		msgVence("PAPEL", "computador")
	else:
		msgVence("TESOURA", "jogador1")
elif jogador1 == "PEDRA":
	msgVence("PEDRA", "jogador1")
else:
	msgVence("TESOURA", "computador")


input()