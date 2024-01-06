import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from numpy.polynomial.polynomial import Polynomial


a,b=-1,1
f = lambda x: 1/(1+25*x*x)
plt.figure(num='Кубические сплайны')

x = np.linspace(a,b,100)
y = f(x)    
plt.plot(x, y,label='График 1/(1+25*x^2)')

for n in [5,10,15]:
    t = np.linspace(a,b,n)
    y = f(t)
    yint = scipy.interpolate.CubicSpline(t, y)

    plt.plot(t, y, 'o')
    plt.plot(x, yint(x), '-',label=f'{n}')
plt.legend()
plt.show()