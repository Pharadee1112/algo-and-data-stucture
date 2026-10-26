N, M, trees = list(map(int, input().split()))

position = []
block = [[False] * M for _ in range(N)]

dp = [[False] * M for _ in range(N)]
dp[0][0] = True

for i in range(trees):
    r, c = map(int, input().split())
    position.append((r, c))

for r, c in position:
    block[r][c] = True

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue

        if block[r][c]:
            continue

        up = False
        left = False

        if i > 0:
            up = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        dp[i][j] = up or left
        
        if dp[N - 1][M - 1]:
            print(-1)





    


