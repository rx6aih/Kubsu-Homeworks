import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return None, None
        else:
            return -c / b, None

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return None, None

    sqrt_discriminant = math.sqrt(discriminant)

    if b >= 0:
        x1 = (-b - sqrt_discriminant) / (2 * a)
    else:
        x1 = (-b + sqrt_discriminant) / (2 * a)

    if sqrt_discriminant == 0:
        return x1, None

    x2 = c / (a * x1)
    return x1, x2

a = 6*pow(10,30)
b = 5*pow(10,30)
c = pow(10,30)

x1, x2 = solve_quadratic(a, b, c)

if x1 is None:
    print("Нет не комплексных корней")
else:
    print("Корень 1:", x1)
    if x2 is not None:
        print("Корень 2:", x2)