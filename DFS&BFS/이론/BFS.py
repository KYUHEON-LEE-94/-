from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    print(queue)
    #현재 노드를 방문 터리
    visited[start] = True
    #큐가 빌때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=', ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            #아직 방문안함?
            if not visited[i]:
                #인접한 원소들 삽입!
                queue.append(i)
                visited[i] = True
                print(queue)
                print(visited)

#각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [], #0번째 인덱스는 사용하지 않는다 (헷갈리지 않게)
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9

bfs(graph, 1, visited)