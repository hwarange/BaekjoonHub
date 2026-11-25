N, M = map(int, input().split())
N_list = list(map(int, input().split()))
for i in range(N):
    if i == 0:
        continue
    N_list[i] = N_list[i]+N_list[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    if i-2 < 0:
        print(N_list[j-1])
    else:
        print(N_list[j-1]-N_list[i-2])
