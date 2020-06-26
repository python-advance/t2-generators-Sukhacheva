"""
Реализовать функцию, возвращающую список чисел ряда Фибоначчи. 

"""

def get_fib_nums_lst(n):
	"""
	n - количество чисел в списке 

	"""
  lst = [0, 1, 1]
  fib1, fib2 = 1, 1
  if n == 0:
    quit()
  if n == 1:
    print(lst[0])
  if n == 2:
    print(lst[0:2])
  else:
    for i in range(3, n):
      fib1, fib2 = fib2, fib1 + fib2
      lst.append(fib2)
  print(lst)
  return lst

n = int(input('Введите количество чисел: '))
get_fib_nums_lst(n)



assert get_fib_nums_lst(0) is None, "неверный аргумент n"

assert get_fib_nums_lst('0') is None, "неверный аргумент n"

assert get_fib_nums_lst(1) == [0], "ряд начинается с 0"
assert get_fib_nums_lst(2) == [0, 1], "ряд длины 2"
assert get_fib_nums_lst(3) == [0, 1, 1], "ряд длины 3"

assert get_fib_nums_lst(5) == [0, 1, 1, 2, 3], "ряд длины 5"

assert get_fib_nums_lst(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34], "ряд длины 10"
