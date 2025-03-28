X=int(input())
line = 1
count = 0
a=0
b=0

while True: # X 해당 line 찾기
    count+=line
    if(X<=count):
        break
    line+=1

if line % 2==0: #짝수
    b=1+count-X
    a=line-count+X


elif line % 2==1: #홀수
    a=1+count-X
    b=line-count+X


print(f'{a}/{b}')