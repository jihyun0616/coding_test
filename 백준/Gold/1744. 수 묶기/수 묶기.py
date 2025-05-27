N=int(input())
num_list=[int(input()) for _ in range(N)]

plus=[]
minus=[]
one=0 # 1은 곱하면 더하는것보다 못하므로 따로

total = 0

for i in num_list: # 음수, 0, 양수 분리
    if(i<=0):
        minus.append(i)
    elif(i>1):
        plus.append(i)
    elif(i==1):
        one+=1

# 양수는 큰 것 부터 두개씩 곱하기
plus.sort(reverse=True)
for i in range(0,len(plus)-1,2): # range(시작, 끝, 증가숫자)
    total+=plus[i]*plus[i+1]
# 홀수개라면 마지막 남은 (슬라이싱 -1은 맨 마지막임) 하나는 그냥 더한다.
if(len(plus)%2==1):
    total+=plus[-1]

# 음수는 작은 것 부터 두개씩 곱하기
minus.sort()
for i in range(0,len(minus)-1,2):
    total+=minus[i]*minus[i+1]
# 홀수개라면 마지막 남은 하나는 그냥 더한다.
if(len(minus)%2==1):
    total+=minus[-1]


# 1은 모두 더하기 
total+=one

print(total)