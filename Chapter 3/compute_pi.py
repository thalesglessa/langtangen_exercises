import matplotlib.pyplot as plt
import numpy as np

N = int(input('Digite n: '))
sum1 = np.zeros(N)
sum2 = np.zeros(N)

for i in range(N):
    fi = 8/((4*i + 1)*(4*i + 3))
    sum1[i] = sum1[i - 1] + fi

fi = 0
for j in range(1, N):
    fi = 6/(j**2)
    sum2[j] = np.sqrt(fi + (sum2[j - 1])**2)

t = np.linspace(0, N, N)
plt.plot(t, np.pi - sum1, "b", t, np.pi - sum2, "r")
plt.axis([0, N, 0, 0.6])
plt.ylabel('Error')
plt.xlabel('Sum of N number')
plt.show()

print(f"The error in Leibniz's scheme is {np.pi - sum1[N-1]}")
print(f"The error in Euler's scheme is {np.pi - sum2[N-1]}")
