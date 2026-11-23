# n,m 받기
n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        parent[root_b] = root_a

def same_group(a, b):
    return find(a) == find(b)

for _ in range(m):
    check, a, b = map(int, input().split())

    if check == 0:
        union(a, b)
    else:
        if same_group(a, b):
            print("YES")
        else:
            print("NO")