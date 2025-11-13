import sys
input = sys.stdin.readline

N = int(input().strip())
T = [0]*(N+2)
P = [0]*(N+2)
for i in range(1, N+1):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

dp = [0]*(N+2)

for i in range(N, 0, -1):
    end = i + T[i]
    if end <= N + 1:
        dp[i] = max(dp[i+1], P[i] + dp[end])
    else:
        dp[i] = dp[i+1]

print(dp[1])
