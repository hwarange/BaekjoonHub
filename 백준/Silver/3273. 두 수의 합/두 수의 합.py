# 수열의 크기
n = int(input())

# 수열에 포함되는 수
n_list = sorted(list(map(int, input().split())))

# 자연수 x
x = int(input())

L = 0
R = n-1
count = 0

while L < R:
    if n_list[L] + n_list[R] < x:
        L += 1
        continue

    elif n_list[L] + n_list[R] == x:
        count += 1

    R -= 1

print(count)