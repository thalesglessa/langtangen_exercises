import numpy as np

def Circunference(r):
  return 2 * np.pi * r

Area = lamda r: np.pi * r**2

R = int(input('Type the circunference radius: '))
print(f"Its circunference is {Circunference(R):.3}cm and its area is {Area(R):.3}cm²")
