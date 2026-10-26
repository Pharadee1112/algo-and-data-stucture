N = int(input())
nail = list(map(int, input().split()))
nail.sort()

inf = 10 ** 8
dp = [inf] * (N + 1)
dp[0] = 0

for i in range(2, N + 1):
    operation_1 = dp[i - 2] + (nail[i - 1] - nail[i - 2])
    operation_2 = inf
    if i >= 3:
        operation_2 = dp[i - 3] + (nail[i - 1] - nail[i - 3])
    dp[i] = min(operation_1, operation_2)

print(dp[N])
