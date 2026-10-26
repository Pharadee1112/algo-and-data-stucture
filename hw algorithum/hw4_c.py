N, M = map(int, input().split())
x = list(map(int, input().split()))

x.sort()


def is_possible(x, distance, num_student):
    last_sit_idx = 0
    num_student -= 1
    for i in range(1, N):
        if x[i] - x[last_sit_idx] >= distance:
            last_sit_idx = i
            num_student -= 1

    if num_student <= 0:
        return True
    return False


def bsearch(x):
    l = 1
    r = max(x)
    while r - l > 1:
        m = (l + r) // 2
        if is_possible(x, m, M):
            l = m
        else:
            r = m
    return l


result = bsearch(x)
print(result)
