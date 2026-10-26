n, a = map(int, input().split())

result = 0
for i in range(1, n + 1):
    if a == 1:
        result = (n * (n + 1)) // 2
        break
    sum = i * (a ** i)
    result += sum


print(result)
