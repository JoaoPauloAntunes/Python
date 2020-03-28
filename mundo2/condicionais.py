nome = input('Nome: ')
if nome == "João":
	print('Ótimo nome!')
elif nome == "Carlos":
	print('Péssimo nome!')
	# comparação analisa se a string da esq. está contida 'na' string da dir.
elif nome in "Rosa Yasmin Margarida":
	print('Nome de flor!')
	# msg não imprimida para a string "João", pois ela entra em uma condicional anterior
elif nome in "Júlia Letícia Mônica João Sebastião":
	print('Nome com acento!')
elif nome in "Marguerida Rivelino Wanessa":
	print('Tem alguma coisa errada no seu nome...')
else:
	print('Ummmm... Sem comentários!')

input()