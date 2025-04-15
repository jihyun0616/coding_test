import sys
N,M=map(int,input().split())

# 입력 받아 저장
monster = dict()
for i in range(1,N+1):
    name = sys.stdin.readline().strip()
    monster[str(i)] = name
    monster[name] = i

for j in range(M):
    q = input()
    print(monster[q])