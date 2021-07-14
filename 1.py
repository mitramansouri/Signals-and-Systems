import numpy as np
import matplotlib.pyplot as plt

N = 22


def f(n):
    return 0.75 ** (n % 22)


print()
a = []

for k in range(N):
    ak = 0
    for l in range(N):
        ak += f(l) * np.exp(-1j * k * l * 2 * np.pi / N)
    a.append(ak / N)
fs = []

for n in range(N):
    alpha = 0
    for k in range(N):
        alpha += a[k] * np.exp(1j * k * 2 * np.pi * n / N)
        print(a[k] * np.exp(1j * k * 2 * np.pi * n / N))
    fs.append(alpha)

x1 = [i for i in range(N)]
y1 = [f(i) for i in x1]
real_y2 = np.real(fs)
imag_y2 = np.imag(fs)
fig, (ax1, ax2, ax3) = plt.subplots(3)

ax1.scatter(x1, y1)
ax2.scatter(x1, real_y2)
ax3.scatter(x1,imag_y2)
plt.show()
