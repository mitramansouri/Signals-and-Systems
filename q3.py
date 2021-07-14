from scipy.fft import fft , ifft
import numpy as np
import matplotlib.pyplot as plt 
import math
# --------------------
# A
#defining function
def h(t):
    return np.exp(-2*abs(t))

#plot has yaxis and xaxis the x is w range the y should be fft 

w_range = np.linspace(-2*np.pi, 2*np.pi, 100)

def fftresponse():
    a = [h(i) for i in w_range]
    y = fft(a)
    return y
plt.title('A - H(jw)')
plt.plot(w_range,fftresponse())
plt.show()

# ----------------------
# B
# function xs(t) = cos(0.1t)
def xs(t):
    return math.cos(0.1*t)

# function xn(t) = 0.03cos(10t)
def xn(t):
    return 0.03*math.cos(10*t)

def xtotal(t):
    return xn(t) + xs(t)

t_range = np.linspace(-2*np.pi, 2*np.pi, 100)
y = [xtotal(i) for i in t_range]
plt.title('B - xtotal')
plt.plot(t_range, y)
plt.show()

# ----------------------
# C
# Y(jw) = X(jw) * H(jw)
# y(t) = F-1[Y(jw)]

Hjw = fftresponse()

def x_jw_fftresponse():
    a = [xtotal(i) for i in t_range]
    y = fft(a)
    return y
Xjw = x_jw_fftresponse()

def Y_jw_product(h_jw, x_jw):
    y_jw = []
    for index in range(len(h_jw)):
        y_jw.append(h_jw[index] * x_jw[index])
    return y_jw
Yjw = Y_jw_product(Hjw, Xjw)

def y_t(x):
    inveresed_fft = ifft(x)
    return inveresed_fft
yt = y_t(Yjw)
plt.title("C - h(t)")
plt.plot(t_range, yt)
plt.show()

# ------------------------
# D




