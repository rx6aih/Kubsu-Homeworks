import numpy as np
import matplotlib.pyplot as plt

n = 1

trueS = 100
def f(x):
    return np.where(x < n, 10 * x / n, 10 * (x - 20) / (n - 20))

x = np.linspace(0, 20, 100)
a = 20 
b = 10 

N = 100

r_x = np.random.uniform(0, a, N)
r_y = np.random.uniform(0, b, N)

M = np.sum(r_y < f(r_x))

S = a * b * M / N

plt.plot(x, f(x), 'tab:orange')
plt.scatter(r_x, r_y)


plt.title(f"N = {N}, S = {S}, AE = {abs(S - trueS):.2f}, RE = {100 * abs(S - trueS) / trueS:.2f}")

plt.legend()
plt.show()