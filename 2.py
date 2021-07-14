import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


def f(x):
    x1 = x % T
    if 2 <= x1 < 6:
        return 0
    return 1


N = 8
T = 8

a = []
b = []
a0 = (1 / T) * integrate.quad(f, 0.0, 8.0)[0]

for i in range(1, N):
    ak = (2 / T) * integrate.quad(lambda l: f(l) * np.cos(i * 2 * np.pi * l / T), 0.0, 8.0)[0]
    bk = (2 / T) * integrate.quad(lambda l: f(l) * np.sin(i * 2 * np.pi * l / T), 0.0, 8.0)[0]
    a.append(ak)
    b.append(bk)

x1 = np.arange(-10, 11, 0.1)
f1 = np.frompyfunc(f, 1, 1)
y1 = f1(x1)

y2 = a0 / 2

fig, ax = plt.subplots(N-1)
for i in range(N - 1):
    y2 += a[i] * np.cos((i + 1) * x1) + b[i] * np.sin((i + 1) * x1)
    ax[i].plot(x1, y2)

plt.show()
