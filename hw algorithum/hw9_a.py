import heapq
from heapq import heappush, heappop

N = int(input())
heap = []
order = 0 # ไว้กันตอนที่ proritie เท่ากัน

for _ in range(N):
    line = input().split()
    if line[0] == "+":
        id, p = int(line[1]), int(line[2])
        heapq.heappush(heap, (-p, order, id))
        order += 1
    else:
        print(heapq.heappop(heap)[2])