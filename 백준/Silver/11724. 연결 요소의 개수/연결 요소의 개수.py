import sys
sys.setrecursionlimit(10**6)  # 재귀 제한
input = sys.stdin.readline

N,M=map(int,input().split())

# 그래프
graph=[[] for _ in range(N+1)] #1부터 시작
for _ in range(M):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) #양방향

# 방문체크
visited = [False]*(N+1)

# dfs 함수 정의
def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            visited[i]=True
            dfs(graph,i,visited)

# 연결개수 구하기 (시작 조건을 다르게 하면 됨!!)
count = 0
for i in range(1,N+1): # 노드 쭉 탐색하면서
    if not visited[i]: # 연결 끊겨서, 방문 못했던 노드들도 탐색 할 수 있게 함
        dfs(graph,i,visited)
        count+=1

print(count)