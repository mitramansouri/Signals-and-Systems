from scipy.fft import fft  
import numpy as np 
import matplotlib.pyplot as plt 
import math , cmath 

#number of samples
N = 22

# signal is x[n] =  (3/4)^n for 0<n<21
def function(x,n):
    return x**n
    print('fuckin works')

# size of the signal 
def display_size():#|X|
    Xaxis = []
    Yaxis = []
    for i in range(N):
        Xaxis.append(i)
        Yaxis.append(function(0.75, i))
    #fast fourier transform
    y = fft(Yaxis)
    lst = []
    for i in range(len(y)):
        lst.append(abs(y[i])) #size 
    #show 
    plt.plot(Xaxis, lst)
    plt.xlabel('W')
    plt.ylabel('X(e^jw)')
    plt.title('SIZE - only from 0 to N')
    plt.show()


# phase of the signal 
def display_phase():
    x = np.arange(-2*(np.pi) , 2*(np.pi), 0.1)
    y = []
    for n in x :
        y.append(0.75*math.sin(n)/(1-0.75*math.cos(n)))

    #show 
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('PHASE')
    plt.show()

# signal itself 
def display_signal():
    w_range = [i for i in range(N)]
    y = [function(0.75,i) for i in range(N)]
    # show 
    plt.title('SIGNAL')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.scatter(w_range, y)
    plt.show()

def Q1():
    display_size()
    display_phase()
    display_signal()

Q1()
