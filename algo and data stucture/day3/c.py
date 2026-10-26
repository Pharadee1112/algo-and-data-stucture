from bisect import bisect_left

n = int(input())
m = list(map(int, input().split()))

inf = 10 ** 6
d = [inf] * (n + 1)
d[0] = -inf
idx_d = [-1] * (n + 1)
parent = [-1] * n
N = len(m)


for i in range(1, N + 1):
    l = bisect_left(d, m[i - 1])
    d[l] = m[i - 1]
    idx_d[l] = i - 1
    parent[i - 1] = idx_d[l - 1]

lis = bisect_left(d, inf) - 1

print((n - lis) * 2)

curr_index = idx_d[lis]
seq_lis = set()

while curr_index != -1:
    seq_lis.add(curr_index)
    curr_index = parent[curr_index]

pickup = list()

for i in range(0, n):
    if i not in seq_lis:
        print(f"u {i - len(pickup)}")
        pickup.append(m[i])

pickup.sort()

for i in pickup:
    print(f"d {i} {i - 1}")
