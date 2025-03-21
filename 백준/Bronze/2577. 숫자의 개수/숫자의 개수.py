A=int(input())
B=int(input())
C=int(input())

mul=list(str(A*B*C))
number=[0,1,2,3,4,5,6,7,8,9]
number_count=[0]*10

for i in range (len(mul)):
    number_count[int(mul[i])]+=1

for i in range(len(number_count)):
    print(number_count[i])
