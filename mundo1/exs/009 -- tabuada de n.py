n = int(input('n: '))
# { n * 0, n * 1, n * 2, ..., n * 10 }
for i in range(0, 11):
	print('{} x {} = {}'.format(n, i, n * i))
input()