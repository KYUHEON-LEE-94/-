# INF = int(1e9) #무한

# #노드의 개수 및 간선의 개수
# n,m,c = map(int, input().split())

# # 2차원 리스트를 만들고 무한으로 초기화
# graph = [[INF]*(n+1) for _ in range(n+1)]

# #자기 자신 -> 자기 자신 비용은 0으로 초기화
# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == c:
#             graph[a][b] = 0

# #각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
# for _ in range(m):
#     #A에서 B로 가는 비용은 C라고 설정
#     x,y,z = map(int, input().split())
#     graph[x][y] = z

# #점화식에 따라 플로이드 워셜 알고리즘을 수행
# for k in range(1, n+1):
#     for a in range(1, n+1):
#         for b in range(1, n+1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# #수행된 결과 출력
# result = ""
# for a in range(1, n+1):
#     for b in range(n, 0, -1):  # 거꾸로 반복
#         # 도달하지 못하는 경우 INF 출력
#         if graph[a][b] == INF:
#             result += "INFINITY "
#         else:
#             if graph[a][b] == 0: pass
#             result += str(graph[a][b]) + " "
#     result += "\n"  # 한 행이 끝날 때마다 개행
# print(result)

#풀이
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수, 시작 노드
n,m,start = map(int, input().split())
#각 노드에 연결되어있는 노드 정보를 담는 리스트
graph = [[]for i in range(n+1)]
#최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    #시작노드 -> 시작 노드 로 가기 위한 최단거리는 0, 큐에 삽입
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        #거리, 현재 노드 = 힙에서 꺼냄
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))



#모든 간선 정보 입력받기
for _ in range(m):
    x,y,z = map(int, input().split())
    #x -> y로 가는 비용이 z
    graph[x].append((y,z))

#다익스트라 알고리즘 수행
dijkstra(start)

#도달가능한 노드 개수
count = 0
#도달 가능한 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    #도달할 수 있는 노드인 경우
    if d != 1e9:
        count +=1
        max_distance = max(max_distance,d)

#시작 노드는 제외해야 하므로 count-1 출력
print(count-1, max_distance)