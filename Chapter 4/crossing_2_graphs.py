import numpy as np

f = lambda x: x
g = lambda x: x**2

N = int(input('Type the number of distributed points: '))
epsilon = float(input('Type epsilon: '))

#Dividing the interval [-4, 4] in N parts
l = np.linspace(-4, 4, N)

for i in range(1, N, 1):
	#Checking and writing when |f(x) - g(x)| < Epsilon
	if abs(f(l[i]) - g(l[i])) < epsilon:
		print(f'f(x) intersects g(x) in x = {l[i]:.1}')
