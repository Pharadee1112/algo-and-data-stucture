W, N = map(int, input().split())
weights = list(map(int, input().split()))
cost = list(map(int, input().split()))

d = [[0] * (W + 1) for i in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, W + 1):
        if weights[i - 1] > w:
            d[i][w] = d[i - 1][w]
        else:
            d[i][w] = max(d[i - 1][w],
            d[i - 1][w - weights[i - 1]] + cost[i - 1])

print(d[N][W])

chosen = []
w = W
for i in range(N, 0, -1):
    if d[i][w] != d[i - 1][w]:
        chosen.append(i)
        w -= weights[i - 1]

chosen.sort()
print(len(chosen))
print(*chosen)
