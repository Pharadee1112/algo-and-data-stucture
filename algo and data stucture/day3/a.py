from bisect import bisect_left


def lis(x):
    N = len(x)
    inf = 10 ** 18
    d = [inf] * (N + 1)

    d[0] = -inf
    for i in range(1, N + 1):
        l = bisect_left(d, x[i - 1])
        d[l] = x[i - 1]

    return bisect_left(d, inf) - 1


n = int(input())
a = list(map(int, input().split()))

print(lis(a))
