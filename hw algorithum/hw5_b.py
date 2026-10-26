import sys

open = { ')': '(', ']':'[','}': '{' }

s = sys.stdin.readline().strip()
stack = []
ok = True
for i in s:
    if i in '([{':
        stack.append(i)
    elif not stack or stack.pop() != open[i]:
        ok = False
        break


