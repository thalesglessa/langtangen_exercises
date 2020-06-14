def sum_vectors(a, b):
	c = []
	c.append(a[0] + b[0])
	return c[0]

a = [0]
b = [0]

a[0] = float(input('The first vector is: '))
b[0] = float(input('The second vector is: '))

if len(a) == len(b):
	print(f'a is {a[0]} and b is {b[0]}, their sum is {sum_vectors(a, b)}')
else:
	print('None')
