minutes, item = map(int, input().split())
a = list(map(int, input().split()))

for i in range(item - 1):
    min_i = i
    for j in range(i + 1, item):
        if a[j] < a[min_i]:
            min_i = j
    a[i], a[min_i] = a[min_i], a[i]

total = 0
count = 0

for i in range(len(a)):
    total += a[i]
    if total > minutes:
        break
    count += 1

print(count)
