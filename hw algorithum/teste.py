m, n = map(int, input().split())
stairs = list(map(int, input().split()))
grasshoppers = list(map(int, input().split()))


def bsearch_r(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


for i in range(n):
    ans = bsearch_r(stairs, grasshoppers[i])

    print(ans, end=' ')
