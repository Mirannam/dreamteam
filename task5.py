a = input('''ваш вопрос-как работает функция reversed 
введите слово   ''')
print(a)
try:
	for i in reversed(a):
		print(i, end='')
except:
	print(a)
