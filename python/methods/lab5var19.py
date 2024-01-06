import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные
x_data = np.array([25, 40, 55, 70, 85, 100])
y_data = np.array([2.4, 3.2, 3.8, 4.3, 4.7, 5.1])

def linear_function(x, a, b): return a * x + b

def power_function(x, a, b): return a * x**b

def exponential_function(x, a, b): return a * np.exp(b * x)

def quadratic_function(x, a, b, c): return a * x**2 + b * x + c


def linear_least_squares(x_d, y_d):
    n = len(x_d)

    # Суммы для вычисления параметров
    sum_x = sum(x_d)
    sum_y = sum(y_d)
    sum_xy = sum(x * y for x, y in zip(x_d, y_d))
    sum_x_squared = sum(x**2 for x in x_d)

    # Вычисление параметров a и b
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    b = (sum_y - a * sum_x) / n

    return a, b


# Используем curve_fit для аппроксимации данных
params_linear, covariance_linear = curve_fit(linear_function, x_data, y_data)
params_power, covariance_power = curve_fit(power_function, x_data, y_data)
params_exponential, covariance_exponential = curve_fit(exponential_function, x_data, y_data)
params_quadratic, covariance_quadratic = curve_fit(quadratic_function, x_data, y_data)

# Создаем массив x для построения графиков
x_fit = np.linspace(min(x_data), max(x_data), 100)

fig, axs = plt.subplots(2)

# Построение графиков
axs[0].scatter(x_data, y_data, label='Экспериментальные данные')
axs[1].scatter(x_data, y_data, label='Экспериментальные данные')

axs[0].plot(x_fit, linear_function(x_fit, *params_linear), label='Линейная функция')
axs[1].plot(x_fit, linear_function(x_fit, *linear_least_squares(x_data, y_data)), label='Линейная функция')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
# plt.title('Аппроксимация методом наименьших квадратов')
plt.show()

# Вывод параметров аппроксимации с округлением до 0,01
print("Линейная функция: a =", round(params_linear[0], 2), "b =", round(params_linear[1], 2))
print("Степенная функция: a =", round(params_power[0], 2), "b =", round(params_power[1], 2))
print("Показательная функция: a =", round(params_exponential[0], 2), "b =", round(params_exponential[1], 2))
print("Квадратичная функция: a =", round(params_quadratic[0], 2), "b =", round(params_quadratic[1], 2), "c =", round(params_quadratic[2], 2))