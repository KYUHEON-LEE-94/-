#2 미로 탈출
from collections import deque

# def bfs(x, y):
#     print(x, y)
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False;

#     queue = deque([])
    
#     result = 0;
#     #현재 노드를 방문 터리
#     if(graph[x][y] == 1):
#          for i in graph[x]:
#             print(i)
#             if i == 0:
#                 queue.append(i)
#                 result += 1
#     print(result)


# n, m = map(int, input().split())

# graph = [];
# for i in range(n):
#     graph.append(list(map(int, input())));
# print("print(graph)", end=' ')
# print(graph)

# #각 노드가 방문된 정보를 표현(1차원 리스트)

# for i in range(1, n+1):
#     for j in (1, m+1):
#         bfs(i, j)

#실패
        
#답안
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    print("queue", end=' ')    
    print(queue)   

    #큐가 빌때까지 반복
    while queue:
        x, y = queue.popleft()
        #현 재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #괴물인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print("graph[nx][ny]", end=' ')    
                print(graph[nx][ny])  
                queue.append((nx, ny))
                print("queue2", end=' ')    
                print(queue)  
    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]

n, m = map(int, input(). split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#이동할 네가지 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS를 수행한 결과 출력
print(bfs(0, 0))