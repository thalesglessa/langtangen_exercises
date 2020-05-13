import numpy as np

N = 6
y = np.zeros(N)

for i in range(len(y)):
    y[i] = np.random.randint(1, 10)
print(y)

for j in range(len(y) - 1):
    for i in range(len(y) - 1):
        if y[i+1] < y[i]:
            y[i], y[i+1] = y[i+1], y[i]
print(y)
