from collections import deque

N,M,V=map(int,input().split())

graph=[[] for _ in range(N+1)] # 빈 리스트 생성, 0제외

for i in range(M): 
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향

for i in range(1,N+1):
    graph[i].sort() # 정렬 (노드 번호가 작은것부터 방문)

visited = [False]*(N+1)  # 0제외

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start]=True
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True # 중복 삽입 방지 위해 추가할 때 방문 처리

dfs(graph,V,visited)
visited = [False]*(N+1)
print()
bfs(graph,V,visited)