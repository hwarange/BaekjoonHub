N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
nums = list(map(int, input().split()))

for n in nums:
    L = 0
    R = N-1

    while L <= R:
        MID = (L+R)//2

        if n == A[MID]:
            print(1)
            break
        elif n < A[MID]:
            R = MID - 1
        else:
            L = MID + 1

    if L > R:
        print(0)
