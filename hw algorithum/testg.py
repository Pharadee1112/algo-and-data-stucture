from collections import deque


def bfs(G, visited, d, p, s):
    vertex_queue = deque([s])
    while vertex_queue:
        v = vertex_queue.popleft()
        visited[v] = 2
        for u in G[v]:
            if not visited[u]:
                visited[u] = 1
                vertex_queue.append(u)
                d[u] = d[v] + 1
                p[u] = v


N, M, s = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(M):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

visited = [0] * N
d = [0] * N
p = [-1] * N

bfs(G, visited, d, p, s)

count = 0

for i in range(N):
    if visited[i]:
        count += 1

print(count)
