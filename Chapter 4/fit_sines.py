import matplotlib.pyplot as plt 
import numpy as np 

f = lambda t: (1/np.pi)*t

def sinesum(t, b):
	Sn = []
	for i in range(0, len(t)):
		a = 0
		for j in range(0, len(b)):
			a += b[j] * np.sin((j+1) * t[i])
		Sn.append(a)
	return Sn 

def test_sinesum():
	n = [4, -3]
	t = [-np.pi/2, np.pi/4]
	return sinesum(t, n)

def plot_compare(f, N, M):
	#N is the array of bn
	t = np.linspace(-np.pi, np.pi, M)
	plt.plot(f(t), t, 'b', sinesum(t, N), t, 'r')
	plt.show()

def error(b, f, M):
	t = np.linspace(-np.pi, np.pi, M)
	e = 0
	Sn = sinesum(t, b)
	for i in range(0, M, 1):
		e += (f(t[i]) - Sn[i])**2
	return np.sqrt(e)

def trial(f, N):
	b = []
	for i in range(0, N, 1):
		a = float(input(f'Type b{i+1}: '))
		b.append(a)
	print(f'The error is {error(b, f, 5)}')
	plot_compare(f, b, 500)

def automatizing(f, N, n):
	#Making the process in f) automatic
	a = 10
	t = np.linspace(-1, 1, n)
	b = np.zeros(N)

	for i in range(0, len(t), 1):
		print(i)
		b[0] = t[i]
		for j in range(0, len(t), 1):
			b[1] = t[j]
			for k in range(0, len(t), 1):
				b[2] = t[k]
				e = error(b, f, 500)
				if e < a:
					a = e
					best = [b[0], b[1], b[2]]
	print(f'The error is {a}, b1 is {best[0]}, b2 is {best[1]} and b3 is {best[2]}')
	plot_compare(f, best, 500)
	

automatizing(f, 3, 21)
