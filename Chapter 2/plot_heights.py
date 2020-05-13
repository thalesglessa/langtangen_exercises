import numpy as np
import matplotlib.pyplot as plt

family1 = np.zeros(4)
family2 = np.zeros(4)
i = np.zeros(4)

family1[0] = 1.60
family1[1] = 1.85 
family1[2] = 1.75
family1[3] = 1.80

family2[0] = 0.50
family2[1] = 0.70
family2[2] = 1.90
family2[3] = 1.75

i[0] = 1
i[1] = 2
i[2] = 3
i[3] = 4

plt.plot(i, family1, "b", i, family2, "r")
# the suggestion may be write as plt.plot(i, family1, "bo", i, family2, "r*")
plt.axis([0,5 , 0,2])
plt.show
