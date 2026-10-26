def permutations(x, perm=None):
    if perm is None:
        perm = []
    if len(x) == 0:
        yield perm
        return
    for i in range(len(x)):
        yield from permutations(x[:i] + x[i + 1:], perm + [x[i]])


N = int(input())
M = int(input())

knows = set()
for _ in range(M):
    a, b = map(int, input().split())
    knows.add((a, b))
    knows.add((b, a))

for perm in permutations(list(range(N))):
    valid = True
    for i in range(N - 1):
        if (perm[i], perm[i + 1]) not in knows:
            valid = False
            break
    if valid:
        print(*perm)
        break
else:
    print('Impossible')
