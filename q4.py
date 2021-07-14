import numpy as np
import matplotlib.pyplot as plt 
from scipy import signal 
from scipy.fft import fft , ifft

t_range = np.arange(-2*np.pi , 2*np.pi , 0.1)
# xt = [x(t) for t in t_range]
# h(t) = e^-t*u(t)
def h(t):
    if t > 0 : 
        return 0 
    else : 
        return np.exp(-t)
# ht = [h(t) for t in t_range]


# plt.title('h(t)')
# plt.plot(t_range,ht)
# plt.show()
# x(t) = pulse between +-B/2
def x(t):
    # B is 2*np.pi
    if -1*np.pi <t and t< np.pi:
        return 1 
    else : 
        return 0 

# xt = [x(t) for t in t_range]

# plt.title('x(t)')
# plt.plot(t_range,xt)
# plt.show()

# y(t) = x(t) conv h(t)
# Y(jw) = X(jw) * H(jw)
# y(t) = F-1{Y(jw)}

def convolution():

    xt = [x(t) for t in t_range]
    ht = [h(t) for t in t_range]

    xjw = fft(xt)
    hjw = fft(ht)

    yjw = []
    
    for index in range(len(hjw)):
        yjw += [xjw[index] * hjw[index]]
    
    yt = ifft(yjw)


    plt.title("Convolution")
    plt.plot(t_range, yt)
    plt.show()

convolution()

