import sys
sys.setrecursionlimit(10**6)

# 정점의 개수 n과 간선의 개수 m(반복문 횟수)
n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

# 연결된 끝점 u, v
for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visited = set()

def dfs(num):
    visited.add(num)
    for i in range(len(graph)):
        if graph[num][i] == 1 and i not in visited:
            dfs(i)

count = 0

for i in range(1, len(graph)):
    if i not in visited:
        dfs(i)
        count += 1

print(count)