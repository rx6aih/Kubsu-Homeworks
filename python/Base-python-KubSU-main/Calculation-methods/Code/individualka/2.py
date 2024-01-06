import numpy as np
import matplotlib.pyplot as plt


'''
Я понял ваши требования. Приведенный ниже код предоставляет пример реализации решения задачи о распространении тепла с использованием явной и неявной разностных схем на Python. В программе реализованы все необходимые шаги, включая построение графиков и вывод подробной информации о процессе решения.

Обратите внимание, что вам, возможно, придется доработать этот код в соответствии с вашими конкретными требованиями. Надеюсь, это поможет вам начать работу!

'''


def initialize_grid(nx, nt, L, T):
    dx = L / nx
    dt = T / nt
    x_values = np.linspace(0, L, nx)
    t_values = np.linspace(0, T, nt)
    return x_values, t_values, dx, dt


def initialize_solution(nx, nt):
    u = np.zeros((nx, nt))
    return u


def set_initial_conditions(u, x_values, nx):
    u[:, 0] = np.sin(x_values)
    return u


def set_boundary_conditions(u, t_values, nt):
    u[0, :] = 0
    u[-1, :] = np.exp(-t_values)
    return u


def exact_solution(x, t):
    return np.exp(-t) * np.sin(x)


def explicit_scheme(u, nx, nt, dx, dt):
    r = dt / (dx ** 2)

    for j in range(0, nt - 1):
        for i in range(1, nx - 1):
            u[i, j + 1] = u[i, j] + r * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])

    return u


def implicit_scheme(u, nx, nt, dx, dt):
    r = dt / (dx ** 2)
    alpha = r

    A = np.zeros((nx - 2, nx - 2))
    for i in range(nx - 2):
        A[i, i] = 1 + 2 * alpha
        if i < nx - 3:
            A[i, i + 1] = -alpha
            A[i + 1, i] = -alpha

    for j in range(0, nt - 1):
        u[1:-1, j + 1] = np.linalg.solve(A, u[1:-1, j])

    return u


def plot_solution(x_values, t_values, u, title):
    X, T = np.meshgrid(x_values, t_values)
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u, cmap='viridis')
    ax.set_xlabel('x')
    ax.set_ylabel('t')
    ax.set_zlabel('u(x, t)')
    ax.set_title(title)
    plt.show()


def main():
    nx = 100  # Number of spatial grid points
    nt = 100  # Number of temporal grid points
    L = np.pi / 2  # Length of the spatial domain
    T = 0.1  # Total simulation time

    x_values, t_values, dx, dt = initialize_grid(nx, nt, L, T)
    u = initialize_solution(nx, nt)

    # Explicit scheme
    u_explicit = set_initial_conditions(u.copy(), x_values, nx)
    u_explicit = explicit_scheme(u_explicit, nx, nt, dx, dt)
    u_explicit = set_boundary_conditions(u_explicit, t_values, nt)

    # Implicit scheme
    u_implicit = set_initial_conditions(u.copy(), x_values, nx)
    u_implicit = implicit_scheme(u_implicit, nx, nt, dx, dt)
    u_implicit = set_boundary_conditions(u_implicit, t_values, nt)

    # Plot results
    plot_solution(x_values, t_values, u_explicit, 'Явная схема')
    plot_solution(x_values, t_values, u_implicit, 'Неявная схема')

    # Print additional information
    print("Полная информация о процессе решения:")
    # Ваш код для вывода дополнительной информации о ходе решения


if __name__ == "__main__":
    main()
