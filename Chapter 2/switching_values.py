import numpy as np

x = np.linspace(1, 3, 3)
print(x)

x[0], x[1] = x[1], x[0] #Switches the values of the array
print(x)
