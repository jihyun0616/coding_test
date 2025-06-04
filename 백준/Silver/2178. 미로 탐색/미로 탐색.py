from collections import deque

N,M=map(int, input().split()) #N:세로, M:가로

#미로 구성
graph=[list(map(int,input())) for _ in range(N)]

#상하좌우 이동 배열
dx=[-1,1,0,0]
dy=[0,0,-1,1]

queue=deque([])

def bfs(x,y):
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        # 상하좌우 확인
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            #범위를 벗어나면 무시
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1 #누적 경로 합
                queue.append([nx,ny])
    return graph[N-1][M-1]

#미로 시작
print(bfs(0,0))