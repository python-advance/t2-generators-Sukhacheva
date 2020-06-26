def get_fib_nums_lst(n):
	"""
	n - количество чисел в списке 

	"""
	def fib(n):
		a, b = 0, 1
		for _ in range(n):
			yield a
			a, b = b, a + b

	if int(n) == 0:
		return None
	return list(fib(n))

print(get_fib_nums_lst(9))
