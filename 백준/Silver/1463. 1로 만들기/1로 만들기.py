X = int(input())

n_list = [i for i in range(X+1)]

n_list[0] = 0
n_list[1] = 0

for i in range(1, X+1):
    if i % 3 == 0:
        n_list[i] = n_list[i//3]+1
    if i % 2 == 0:
        n_list[i] = min(n_list[i], n_list[i//2]+1)
    n_list[i] = min(n_list[i], n_list[i-1]+1)


print(n_list[X])