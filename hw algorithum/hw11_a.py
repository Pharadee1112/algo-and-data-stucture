N = int(input())
element = list(map(int, input().split()))

element.sort(reverse=True)

valid = True
for i in range(N):
    if element[i] % element[i + 1] != element[i + 2]:
        valid = False
        break
        
if valid and element[0] > element[1]:
    print(element[0], element[1])
else:
    print(-1)
