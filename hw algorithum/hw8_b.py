N = int(input())
costs = list(map(int, input().split()))

total = sum(costs)

if total % 2 == 1:
    print("NO")
else:
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for ci in costs:
        for s in range(target, ci - 1, -1):
            if dp[s - ci]:
                dp[s] = True

    print("YES" if dp[target] else "NO")
