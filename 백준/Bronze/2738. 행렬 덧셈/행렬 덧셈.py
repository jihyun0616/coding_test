N, M = map(int, input().split())

A=list()
B=list()
inputValue=list()

for i in range(N): #A에 list로 저장
    inputValue = list(map(int, input().split()))
    A.append(inputValue)

for i in range(N): #B에 list로 저장
    inputValue = list(map(int, input().split()))
    B.append(inputValue)


for i in range(N): #출력
    for j in range(M):
        print(f'{A[i][j]+B[i][j]} ',end="")
    print()
