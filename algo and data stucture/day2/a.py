a, b, c, d = map(int, input().split())

if a < 0:
    s = -1
else:
    s = 1


def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d


l = -10 ** 8
r = 10 ** 8

eps = 10 ** -6

while r - l > eps:
    m = (l + r) / 2
    if f(m) * s < 0:
        l = m
    else:
        r = m
print(f'{m: .6f}')
