import numpy as np
import matplotlib.pyplot as plt
'''
Mitra's std_num = 9732529
Abdolrahim's std_num = 9732508
Mohammad's std_num = 9732513
'''
# a = yekan 
a = (9 + 8 + 3) / 3
# b dahgan
b = (2 + 0 + 1) / 3
x1 = np.arange(-8, 8, 0.01)
y1 = np.sin(np.pi * (x1 * a + b)) / (np.pi * (x1 * a + b))

plt.plot(x1, y1)
plt.show()
