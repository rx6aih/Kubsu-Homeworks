import math

n=int(input("Количество операций : "))

row1=0
for i in range(1,n+1):
    row1+=1/(math.pow(i,2)+1)
print("Результат обычного ряда для "+str(n)+" операций равен " + str(row1))

row2=0
for i in range(1,n+1):
    row2+=1/(math.pow(i,4)*(math.pow(i,2)+1))
row2=(math.pow(math.pi,2)/6)-(math.pow(math.pi,4)/90)+row2

print("Результат ряда с использованием преобразования для "+str(n)+" операций = "+str(row2))

print("Разница = "+str(row2-row1))