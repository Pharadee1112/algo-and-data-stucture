from collections import deque


def bfs(G, visited, s):
    vertex_queue = deque([s])
    component = []
    while vertex_queue:
        v = vertex_queue.popleft()
        if not visited[v]:
            visited[v] = True
            component.append(v)
            for u in G[v]:
                if not visited[u]:
                    vertex_queue.append(u)
    return component


n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [False] * n
components = []

for i in range(n):
    if not visited[i]:
        components.append(bfs(G, visited, i))

print(len(components))
for comp in components:
    print(len(comp))
    print(*comp)
