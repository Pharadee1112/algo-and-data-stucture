def subsets(x, subset=None):
    if subset is None:
        subset = []
    if len(x) == 0:
        yield subset
    else:
        yield from subsets(x[1:], subset)
        yield from subsets(x[1:], subset + [x[0]])


H, N = map(int, input().split())
h = list(map(int, input().split()))

for s in subsets(h):
    if sum(s) == H:
        print(*s)
        break
else:
    print('Impossible')
