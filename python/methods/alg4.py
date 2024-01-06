import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, x0, tolerance=1e-6, max_iterations=1000):
    n = len(b)
    x = np.copy(x0)
    residuals = []

    for k in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x_old[:i]) + np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]

        residual = np.linalg.norm(np.dot(A, x) - b)
        residuals.append(residual)

        if residual < tolerance:
            break

    return x, residuals

def gauss_seidel(A, b, x0, tolerance=1e-6, max_iterations=1000):
    n = len(b)
    x = np.copy(x0)
    residuals = []

    for k in range(max_iterations):
        x_old = np.copy(x)
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sigma) / A[i, i]

        residual = np.linalg.norm(np.dot(A, x) - b)
        residuals.append(residual)

        if residual < tolerance:
            break

    return x, residuals

# Уравнения СЛАУ
A = np.array([[12.14, 1.32, -0.78, -2.75],
              [-0.89, 16.75, 1.88, -1.55],
              [2.65, -1.27, -15.64, -0.64],
              [2.44, 1.52, 1.93, -11.43]])

b = np.array([14.78, -12.14, -11.65, 4.26])

# Начальное приближение
x0 = np.zeros_like(b)

# Решение методом Якоби
solution_jacobi, residuals_jacobi = jacobi(A, b, x0)

# Решение методом Зейделя
solution_seidel, residuals_seidel = gauss_seidel(A, b, x0)

# Вывод решений
print("Решение методом Якоби:", solution_jacobi)
print("Решение методом Зейделя:", solution_seidel)

# Построение графика
iterations_jacobi = range(1, len(residuals_jacobi) + 1)
iterations_seidel = range(1, len(residuals_seidel) + 1)

plt.plot(iterations_jacobi, residuals_jacobi, label='Якоби')
plt.plot(iterations_seidel, residuals_seidel, label='Зейдель')

plt.yscale('log')  # логарифмическая шкала для нормы невязки
plt.xlabel('Номер итерации')
plt.ylabel('Норма невязки')
plt.legend()
plt.show()
