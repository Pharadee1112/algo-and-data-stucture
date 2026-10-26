n, m = map(int, input().split())
time = list(map(int, input().split()))
time.sort()

count = 0
count_index = 0

for i in range(n):
    count += time[i]
    if count <= m:
        count_index += 1
    else:
        break

print(count_index)
