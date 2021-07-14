import numpy as np
import matplotlib.pyplot as plt

a = (3 + 3 + 3) / 3
b = (1 + 1 + 1) / 3
x1 = np.arange(-8, 8, 0.01)
y1 = np.sin(np.pi * (x1 * a + b)) / (np.pi * (x1 * a + b))

plt.plot(x1, y1)
plt.show()
