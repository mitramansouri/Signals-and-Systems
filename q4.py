import numpy as np
import matplotlib.pyplot as plt 
from scipy.fft import fft , ifft
import sympy as sy
from scipy.integrate import quad
t_range = np.arange(-2 * (np.pi), 2 * (np.pi), 0.1)

# xt = [x(t) for t in t_range]
# h(t) = e^-t*u(t)
def h(t):
    if t < 0 : 
        return 0 
    else : 
        return np.exp(-t)

def h_prime(tprime):
    if tprime > 0 : 
        return 0 
    else : 
        return np.exp(-tprime)
ht = [h(t) for t in t_range]

plt.title('h(t)')
plt.plot(t_range,ht)
plt.show()

# x(t) = pulse between +-B/2
def x(t):
    # B is 2*np.pi
    if -1*np.pi <t and t< np.pi:
        return 1 
    else : 
        return 0 

xt = [x(t) for t in t_range]

plt.title('x(t)')
plt.plot(t_range,xt)
plt.show()

def integrand(tav , t):
    return x(tav)*h(t-tav)

def convolution():

    # h(t) --> h(t-T) 
    # x(t) --> x(T)
    yt = []
    for t in t_range:
        # print(t)
        # if t< -1*np.pi :
        #     # no overlap 
        #     yt.append(0)
        # elif  -1*np.pi <t and t< np.pi:
        #     # integral of the overlapped parts
        #     # yt.append(sy.integrate(h_prime(tav), (tav, -1*np.pi, t)))
        #     yt.append(quad(h_prime , -1*np.pi, t , args=())[0])
        # elif  t> np.pi :
        #     # integral of the overlapped parts
        #     # yt.append(sy.integrate(h_prime(tav), (tav, t,np.pi)))   
        #     yt.append(quad(h_prime , t, np.pi , args=())[0])
        yt.append(quad(integrand , -np.inf , np.inf , args=(t))[0])


    plt.title("Convolution")
    plt.plot(t_range, yt)
    plt.show()

convolution()

