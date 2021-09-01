while True:
	math = input("Нажмите на + или - или * или /: ")
	f_num = float(input("Введите число: "))
	s_num = float(input("Введите число: "))
	if math == "+":
		print(f_num + s_num)
	elif math == "-":
		print(f_num - s_num)
	elif math == "*":
		print(f_num * s_num)
	elif math == '/':
		if s_num != 0:
			print(f_num / s_num)
		else:
			print("Деление на ноль")
	else:
		print("error")
	con = input("Хотите завершить: y ot n")
	if con == 'y':
		break
