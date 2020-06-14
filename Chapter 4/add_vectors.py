def sum_vectors(a, b):
	if len(a) == len(b):
		c = []
		c.append(a[0] + b[0])
		return c[0]
	else:
		return None

a = [0]
b = [0]

a[0] = float(input('The first vector is: '))
b[0] = float(input('The second vector is: '))

print(f'a is {a[0]} and b is {b[0]}, their sum is {sum_vectors(a, b)}')
