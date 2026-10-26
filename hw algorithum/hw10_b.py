from collections import deque


def bfs(grid, visited, s, n, m):
    vertex_queue = deque([(s[0], s[1], 0)])
    dirs = [(-1,0), (1, 0), (0, -1), (0, 1)]
    while vertex_queue:
        r, c, d = vertex_queue.popleft()
        if not visited[r][c]:
            visited[r][c] = True
            if grid[r][c] == 'X':
                return d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc] != '#':
                    vertex_queue.append((nr, nc, d + 1))
    return -1


n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(input())

visited = [[False] * m for _ in range(n)]
sr, sc = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'E':
            sr, sc = i, j

print(bfs(grid, visited, (sr, sc), n, m))
