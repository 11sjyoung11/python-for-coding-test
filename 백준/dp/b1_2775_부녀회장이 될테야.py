import sys

input = sys.stdin.readline

T = int(input().strip())
queries = []
max_k = max_n = 0
for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    queries.append((k, n))
    max_k = max(max_k, k)
    max_n = max(max_n, n)

# dp[k][n]: k층 n호 거주민 수
dp = [[0] * (max_n + 1) for _ in range(max_k + 1)]

# 0층: i호에 i명
for i in range(1, max_n + 1):
    dp[0][i] = i

# 각 층 1호는 1명
for k in range(1, max_k + 1):
    dp[k][1] = 1
    for n in range(2, max_n + 1):
        dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

for k, n in queries:
    print(dp[k][n])
