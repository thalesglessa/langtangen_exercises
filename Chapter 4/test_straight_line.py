import numpy as np

f = lambda x: 4*x + 1

derivative = lambda a, b: (f(a) - f(b))/(a - b)

def check(interval, c, a):
	i = 0
	while i < len(interval):
		if interval[i] == c:
			i += 1
		else:
			if derivative(interval[i], c) != a:
				print(f'At x = {interval[i]} and f(x) = {f(interval[i])}, the slope is {derivative(interval[i], c):.2}')
		i += 1


a = int(input('The coeficient is equal to: '))

N = 100
interval = np.linspace(0, 10, N)
np.random.shuffle(interval)

check(interval, 2, a)
