import math
import copy
from math import erf
 
  
# Проверка матрицы коэффициентов на корректность
def isCorrectArray(a):
    for row in range(0, len(a)):
        if( len(a[row]) != len(b) ):
            print('Не соответствует размерность')
            return False
    
    for row in range(0, len(a)):
        if( a[row][row] == 0 ):
            print('Нулевые элементы на главной диагонали')
            return False
    return True

def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += ( x_new[k] - x_old[k] ) ** 2
        sum_low += ( x_new[k] ) ** 2
        
    return math.sqrt( sum_up / sum_low ) < eps
 
def solution(a, b):
    if( not isCorrectArray(a) ):
        print('Ошибка в исходных данных')
    else:
        count = len(b) # количество корней
        
        x = [1 for k in range(0, count) ] # начальное приближение корней
        
        numberOfIter = 0  # подсчет количества итераций
        MAX_ITER = 100    # максимально допустимое число итераций
        while( numberOfIter < MAX_ITER ):
 
            x_prev = copy.deepcopy(x)
            
            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if( j != k ): S = S + a[k][j] * x[j] 
                x[k] = b[k]/a[k][k] - S / a[k][k]
            
            if isNeedToComplete(x_prev, x) : # проверка на выход
                break
              
            numberOfIter += 1
        return x

a = [[1.00, 0.80, 0.64],
     [1.00, 0.90, 0.81],
     [1.00, 1.10, 1.21]]
     
b = [erf(0.8), erf(0.9), erf(1.1)]
 
a2 = [[0.1, 0.2, 0.3],
     [0.4, 0.5, 0.6],
     [0.7, 0.8, 0.9]]
     
b2 = [0.1, 0.3, 0.5]

def my_erf(x):
    erf = 0
    n = 100
    for i in range(1, n + 1):
        erf += (math.pow((-1), i) * math.pow(x, (2 * i) + 1)) / (math.factorial(i) * ((2 * i) + 1))
    erf *= 2 / math.sqrt(math.pi)
    return erf


xxa1=solution(a,b)
xa1=0
for i in range(0,len(xxa1)):
    xa1+=xxa1[i]
print( 'Решение(1) : ', solution(a, b),' , x1+x2+x3 = ',xa1,' erf = ',my_erf(1) )
print('Решение(2) : ',solution(a2,b2))