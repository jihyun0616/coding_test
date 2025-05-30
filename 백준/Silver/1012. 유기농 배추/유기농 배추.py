import sys
sys.setrecursionlimit(10000)  # 재귀 제한

T=int(input()) # 테스트 케이스 개수

for _ in range(T):
    M,N,K=map(int,input().split())
    graph=[[0]*M for _ in range(N)] # 밭

    for _ in range(K):
        x,y=map(int,input().split()) # 배추 위치
        graph[y][x]=1
    
    def dfs(y,x):
        if x<0 or x>=M or y<0 or y>=N: # 범위 벗어나면 종료(false 반환)
            return False
        if graph[y][x]==1:  # 방문처리
            graph[y][x]=0
            dfs(y-1,x)
            dfs(y+1,x)
            dfs(y,x-1)
            dfs(y,x+1)
            return True
        return False
    total=0

    for x in range(M):
        for y in range(N):
            if dfs(y,x)==True:
                total+=1
    
    print(total)




