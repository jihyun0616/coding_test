from collections import deque


# 가장 빠른 시간 탐색 -> BFS (최단거리, 최소 횟수 등)
# DFS는 돌아가므로 시간 낭비 가능 -> 모든 경로 탐색 등

start,end=map(int,input().split())

# 그래프
graph=[0]*100001
visited=[0]*100001 # 각 점별 도달 시간 체크


# bfs 구현
def bfs(start):
    queue = deque([])
    queue.append(start)
    visited[start] = 1 # 시작 시간 1초

    while queue:
        now = queue.popleft()
        if now==end:
            print(visited[now]-1) # 시작시간 1초로 설정했으므로 -1
            return

        for next in [now-1,now+1,now*2]: # 핵심 로직!!
            if 0<=next<100001 and visited[next]==0:
                queue.append(next)
                visited[next]=visited[now]+1 # 누적 시간

bfs(start)
