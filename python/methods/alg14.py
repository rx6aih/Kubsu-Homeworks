import math

n=int(input("Количество операций : "))
i1=0
i2=0

row1=0
for i in range(1,n+1):
    row1+=1/(math.pow(i,2)+1)
    if(i>1):
        if(row1-row3<math.pow(math.exp(1),-5)):
            i1=i
            print("Результат обычного ряда для "+str(n)+" операций равен " + str(row1) + " и сходится на "+str(i1))
            break
    row3=row1
    
row2=0
for i in range(1,n+1):
    row2+=1/(math.pow(i,4)*(math.pow(i,2)+1))
    if(i>1):
        if(row2-row4<math.pow(math.exp(1),-5)):
            i2=i
            print("Ряд после преобразований сходится на "+str(i2))
            break
    row4=row2
row2=(math.pow(math.pi,2)/6)-(math.pow(math.pi,4)/90)+row2

print("Результат ряда с использованием преобразования для "+str(n)+" операций = "+str(row2))

print("Разница = "+str(row2-row1))