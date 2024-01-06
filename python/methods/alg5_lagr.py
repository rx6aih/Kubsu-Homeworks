import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from numpy.polynomial.polynomial import Polynomial


a,b=-1,1
f = lambda x: 1/(1+25*x*x)
plt.figure(num='Лагранж')

x = np.linspace(a,b,100)
y = f(x)
plt.plot(x, y,label='График 1/(1+25*x^2)')

for n in [20,30]:
    t = np.cos(np.pi*(2*np.arange(1,n+1)-1)/(2*n))
    y = f(t)
    yint = Polynomial(scipy.interpolate.lagrange(t, y).coef[::-1])
    
    plt.plot(t, y, 'o')
    plt.plot(x, yint(x), '-',label=f'{n}')
plt.legend()
plt.show()