def safe_print_list(my_list, x):
	try:
		count = 0
		for element in my_list:
			if (count < x):
				print(element, end=' ')
				count += 1
		print('')
		return count
	except:
		print('Index error')