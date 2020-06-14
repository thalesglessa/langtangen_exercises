def Average(N):
	sum = 0
	for i in range(1, N + 1, 1):
		sum = sum + i
	return sum/N

Number = int(input('Type an integer: '))
print(f'The average of 1 to {Number} is {Average(Number)}')
