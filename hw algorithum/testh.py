N = int(input())
items = list(map(int, input().split()))

items.sort()

answer = 0

for k in range(N):
    i = 0
    j = N - 1
    
    while i < j:
        if i == k:
            i += 1
            continue
        if j == k:
            j -= 1
            continue
        current_sum = items[i] + items[j]
        if current_sum < items[k]:
            i += 1
        elif current_sum > items[k]:
            j -= 1
        else:
            answer += 1
            break

print(answer)
