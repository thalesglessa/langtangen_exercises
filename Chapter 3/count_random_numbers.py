import numpy as np

N = int(input('How many numbers would you like?'))
N = np.random.randint(1, 7, N)

M = 0
for i in range(len(N-1)):
    if N[i] == 6:
        M += 1

print(M)
