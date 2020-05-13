import numpy as np
import matplotlib.pyplot as plt

L = np.linspace(1, 3, 3)   #Lenght of the cubes
V = L**3                   #Volume of the cubes
 
plt.plot(L, V)  
plt.xlabel('Lenght (cm)')
plt.ylabel('Volume (cm³)')
plt.show
