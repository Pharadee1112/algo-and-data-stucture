N = int(input())
gears = list(map(int, input().split()))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b // gcd(a, b)


ans = 1
for i in range(1, N):
    ans = lcm(ans, gears[i] // gcd(gears[0], gears[i]))
print(ans)
