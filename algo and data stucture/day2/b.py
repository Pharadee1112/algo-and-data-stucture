vb, vw = map(int, input().split())
a = float(input())


def T(x):
    return ((x * x + (1 - a) ** 2) ** 0.5) / vb + (((1 - x) ** 2 + a * a) ** 0.5) / vw


eps = 10 ** (-8)

r = 1.0
l = 0.0

while r - l > eps:
    m1 = (2 * l + r) / 3
    m2 = (l + 2 * r) / 3
    if T(m1) < T(m2):
        r = m2
    else:
        l = m1

print(f"{(l + r) / 2: .9f}")
