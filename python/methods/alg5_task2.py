import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from numpy.polynomial.polynomial import Polynomial

x = np.array([2,3,5,7])
f = np.array([4,-2,6,-3])


def g(a):
    tck = scipy.interpolate.splrep(x, f)
    return scipy.interpolate.splev(a, tck)

a,b=2,7
plt.figure(num='Кубические сплайны')

y = f  
plt.plot(x, y, 'o')

yint = scipy.interpolate.CubicSpline(x, y, bc_type='clamped')
t = np.linspace(a,b,100)
plt.plot(t, yint(t), '-',label=f'{100}')
plt.legend()
plt.show()