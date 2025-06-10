import sys
input = sys.stdin.readline

N=int(input())
coordinate=list(map(int,input().split())) #좌표
new_coordinate = sorted(list(set(coordinate))) #중복 제거(set 사용) 및 오름차순 정렬

# new_coordinate의 인덱스가 곧 x'i가 됨
# for i in coordinate:
#     print(new_coordinate.index(i),end=' ') # index는 시간초과

dic = {}
for i in range(len(new_coordinate)):
    dic[new_coordinate[i]]=i

for i in coordinate:
    print(dic[i],end=' ')