name = input()
N = int(input())

found = False
for i in range(N):
    a = input()
    if a == name:
        found = True

if found:
    print("Yes")
else:
    print("No")
