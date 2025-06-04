from collections import deque

#BFS로 풀면 될듯
#모두 방문처리가 되었을때, count 몇번 해야하는지

M,N=map(int,input().split()) # M:가로 , N:세로

# 토마토 밭 생성
graph=[list(map(int,input().split())) for _ in range(N)] 

# queue에 익은 토마토 좌표 append
queue=deque([])
for i in range(N):
    for j in range(M):
        if graph[i][j]==1:
            queue.append([i,j])

# 이동 방향, 상하좌우 (가독성 높이기 위한 코드)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


# bfs 함수
def bfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4): # 상하좌우 점검
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M: #범위를 벗어나면 무시
                continue
            if graph[nx][ny]==0: #만약 토마토가 익지 않았다면
                graph[nx][ny]=graph[x][y]+1 #익히자!(날짜 누적)
                queue.append([nx,ny])

bfs() # 익히자

# 결과 출력
res = 0
for i in graph:
    if 0 in i:
        print(-1)
        exit()
    res = max(res,max(i))

print(res-1)
