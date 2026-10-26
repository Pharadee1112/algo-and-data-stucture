w, h, n = map(int, input().split())

def find_board(s):
    return (s // h) * (s // w) >= n


def binary_seacrch_function():
    l = 0
    r = max(w, h) * n
    while r - l > 1:
        m = (l + r) // 2
        if find_board(m):
            r = m
        else:
            l = m
    print(r)

binary_seacrch_function()
