import sys
sys.setrecursionlimit(10**6)

# 컴퓨터의 수
n = int(input())
# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수 => 반복문
connect_count = int(input())
# 인접 행렬로 표현한 그래프 0번 인덱스는 사용안함
computers = [[0]*(n+1) for _ in range(n+1)]

# 인접 행렬로 해당하는 부분을 1로 채워넣음
for i in range(connect_count):
    a, b = map(int, input().split())
    computers[a][b] = 1
    computers[b][a] = 1

visited = []

def dfs(num):
    # 방문기록
    visited.append(num)
    for i in range(len(computers)):
        # 1이면서 방문하지 않았을 때
        if computers[num][i] == 1 and i not in visited:
            dfs(i)

dfs(1)

print(len(visited)-1)
    
