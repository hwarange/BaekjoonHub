# 내 친구의 친구는 내 친구이다.
# 내 원수의 원수도 내 친구이다

# n은 학생의 수
n = int(input())

friend = list(range(n+1))
enemy = list(range(n+1))

def find(x):
    while friend[x] != x:
        friend[x] = friend[friend[x]]
        x = friend[x]
    return x

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:
        friend[root_b] = root_a



# m은 알려진 학생의 인간관계 : 반복문 횟수
m = int(input())

# E는 둘이 원수 F는 둘이 친구

for _ in range(m):
    check, a, b = input().split()
    a = int(a)
    b = int(b)

    if check == "E":
        if enemy[a] != a:
            union(enemy[a], b)
        if enemy[b] != b:
            union(enemy[b], a)
        enemy[a] = b
        enemy[b] = a

    else:
        union(a, b)

# 그거 아세요? 컴프리헨션은 리스트뿐만아니라 SET도(DICT도 가능) 가능합니다
print(len({find(i) for i in range(1, n+1)}))