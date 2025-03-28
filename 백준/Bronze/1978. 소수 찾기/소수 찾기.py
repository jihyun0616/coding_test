import sys

N=int(input())
number_list=list(map(int,sys.stdin.readline().strip().split()))
count=0

for i in number_list:
    if(i==1):
        continue
    for j in range(2,i+1):
        if(i!=j and i%j==0): # 자기 자신(i)이 아닌 다른 수로 나누어 떨어진다면 소수가 아님
            break # 한 경우의 수라도 존재하면 반복문 탈출 -> count X
        elif(i==j and i%j==0): # 자기 자신과 같은 수로 나누어 떨어진다면 소수임
            count+=1 # count +=1

print(count)