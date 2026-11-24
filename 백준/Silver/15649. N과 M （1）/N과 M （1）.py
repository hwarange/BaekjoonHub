# N과 M입력받기
N, M = map(int, input().split())
visited = []

def dfs():
    if len(visited) == M:
        for n in range(M):
            print(visited[n], end=" ")
        print()
        return

    for i in range(1, N+1):
        if i not in visited:
            visited.append(i)
            dfs()
            visited.pop()

dfs()