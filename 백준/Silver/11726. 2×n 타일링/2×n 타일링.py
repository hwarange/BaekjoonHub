N = int(input())

dp = [i for i in range(N+1)]

if N >= 3:
    for i in range(3, N+1):
        dp[i] = (dp[i-1]+dp[i-2])%10_007

print(dp[N])