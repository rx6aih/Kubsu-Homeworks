import numpy as np
import math

def makeIdentity(matrix):
    # перебор строк в обратном порядке 
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            # вычитать строки не нужно, так как в row только два элемента отличны от 0:
            # в последней колонке и на диагонали
            
            # вычитание в последней колонке
            upper_row[-1] -= factor*row[-1]
            # вместо вычитания 1*factor просто обнулим коэффициент в соотвествующей колонке. 
            upper_row[nrow] = 0
    return matrix

def makeTrianglePivot(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            # matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
            matrix[nrow], matrix[pivot] = matrix[pivot], np.copy(matrix[nrow])
        row = matrix[nrow]
        divider = row[nrow] # диагональный элемент
        if abs(divider) < 1e-10:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            raise ValueError("Матрица несовместна")
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow] # элемент строки в колонке nrow
            lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    return matrix

def gaussSolvePivot(A, b):
    """Решает систему линейных алгебраических уравнений Ax=b
    Если b is None, то свободные коэффициенты в последней колонке"""
    shape = A.shape
    assert len(shape) == 2, ("Матрица не двумерная", shape) # двумерная матрица
    A = A.copy()
    if b is not None:
        assert shape[0] == shape[1], ("Матрица не квадратная", shape)
        assert b.shape == (shape[0],), ("Размерность свободных членов не соответствует матрица", shape, b.shape)
        # добавляем свободные члены дополнительным столбцом
        A = np.c_[A, b]
    else:
        # Проверяем, что квадратная плюс столбец
        assert shape[0]+1 == shape[1], ("Неверный формат матрицы", shape)
    makeTrianglePivot(A)
    makeIdentity(A)
    return A[:,-1]

def nevz(A, x, b):
    # Проверка размерностей матрицы A и векторов x, b
    n = A.shape[0]
    if A.shape[1] != n or x.shape[0] != n or b.shape[0] != n:
        raise ValueError("Некорректные размерности матрицы или векторов!")

    # Вычисление вектора невязки
    residual = np.dot(A, x) - b

    for i in range(0, len(residual)):
        print("d", i + 1, "=", "%.16f" % (residual[i]))
    
#Первая система
a1=np.array([[10**-4,1],
            [1,2]])

b1=np.array([1,4])

print(gaussSolvePivot(a1,b1))
nevz(a1,gaussSolvePivot(a1,b1),b1)

print('------------------------------')
#Вторая система
a2=np.array([[2.34,-4.21,-11.61],
     [8.04,5.22,0.27],
     [3.92,-7.99,8.37]])

b2=np.array([14.41,-6.44,55.56])

print(gaussSolvePivot(a2,b2))
nevz(a2,gaussSolvePivot(a2,b2),b2)

print('------------------------------')
#Третья система
a3=np.array([[4.43,-7.21,8.05,1.23,-2.56],
             [-1.29,6.47,2.96,3.22,6.12],
             [6.12,8.31,9.41,1.78,-2.88],
             [-2.57,6.93,-3.74,7.41,5.55],
             [1.46,3.62,7.83,6.25,-2.35]])
b3=np.array([2.62,-3.97,-9.12,8.11,7.23])
print(gaussSolvePivot(a3,b3))
nevz(a3,gaussSolvePivot(a3,b3),b3)
