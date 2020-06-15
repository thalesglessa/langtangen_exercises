f = lambda a, b, x: a*x + b

def error(a, b, t):
	e = 0
	for i in range(0, len(measurements), 1):
		e += (f(a, b, i) - t[i])**2
	return e

measurements = (0.5, 2.0, 1.0, 1.5, 7.5)

i = 1
while i > 0:
	a = float(input('Type a: '))
	b = float(input('Now type b: '))
	print(f"The error is {error(a, b, measurements)}\n")

#a is 1.35 and b is -0.25
