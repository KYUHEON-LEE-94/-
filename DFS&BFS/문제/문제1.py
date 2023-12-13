
# row, column = map(int, input().split())
# print(column)

# graph = [[]];
# for _ in range(0, row):
#     oneRow = list(map(int, input().strip()))
#     graph.append(oneRow);

# print(graph)
# visited = [[0]*column for _ in range(0,row)]
# print(visited)

# def dfs(graph, v, visited):

#     visited[v] = 1
#     print(v)

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# dfs(graph, 1, visited)
# 실패.. #

# 답안지
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False;
    #현재 노드를 아직 방문하지 않았다면
    print("graph[x][y]: ", end='')
    print(graph[x][y])
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
            #방문처리를 수행할 목적으로 호출됨!!
        dfs(x - 1 , y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().split())

#2 차원 리스트의 맵 정보 입력받기
graph = [];
for i in range(n):
    graph.append(list(map(int, input())));
print("print(graph)", end=' ')
print(graph)

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 DFS 수행 -> 위의 상,하,좌,우 계산도 하기떄문에 한번 방문한 노드의 주위 노드도 전부 방문처리됨
        if dfs(i, j) == True:
            result +=1

            
print(result)



