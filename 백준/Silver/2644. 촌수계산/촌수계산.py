n=int(input()) # 사람 (노드)

p1,p2=map(int,input().split()) # 계산해야하는 번호

m = int(input()) # 연결 (간선)

# 그래프 설정
graph=[[] for _ in range(n+1)] # 0 제외 n 포함
for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 설정
visited = [False]*(n+1) # 0제외 n 포함

# dfs 로직 + 촌수 검증
def dfs(graph,start,p2,visited,count):
    if(start==p2):
        return count 
    
    visited[start]=True

    for i in graph[start]:
        if not visited[i]:
            visited[i]=True
            res = dfs(graph,i,p2,visited,count+1) # 촌수 계산 count+1
            if res!=-1:
                return res

    return -1 #연결되어있지 않으면 -1

print(dfs(graph,p1,p2,visited,0))
