import heapq
enterprises = list(map(int, input().split()))

heapq.heapify(enterprises)
tax = 0.0

for _ in range(len(enterprises) - 1):
    a = heapq.heappop(enterprises)
    b = heapq.heappop(enterprises)
    merged = a + b
    tax += merged * 0.05
    heapq.heappush(enterprises, merged)

print(f"{tax:.10f}")