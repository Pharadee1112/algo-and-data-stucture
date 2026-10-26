def sift_up(data, i):
    if i == 0:
        return

    parent = (i - 1) // 2
    if data[parent] < data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def sift_down(data, i):
    child1 = i * 2 + 1
    child2 = i * 2 + 2
    if child1 >= len(data):
        return
    if child2 >= len(data):
        child_max = child1
    else:
        child_max = child1 if data[child1] > data[child2] else child2
    if data[child_max] > data[i]:
        data[i], data[child_max] = data[child_max], data[i]
        sift_down(data, child_max)


def heapify(data):
    for i in range(len(data) - 1, -1, -1):
        sift_down(data, i)


def heappush(data, x):
    data.append(x)
    sift_up(data, len(data) - 1)


def heappop(data, i=0):
    data[i], data[-1] = data[-1], data[i]
    res = data.pop()
    sift_up(data, i)
    sift_down(data, i)
    return res


"""
N = จำนวนหนังสือในตู้
K = จำนวนหนังสือสูงสุดที่วางบนโต๊ะได้
M = ความยาวของรายการที่จะใช้
"""

N, K, M = map(int, input().split())
reading_list = list(map(int, input().split()))

inf = 1000000

use_book = set(reading_list)

next_occurrence = [inf] * M
book_on_table = set()
last_seen = dict()
for i in range(M - 1, -1, -1):
    book = reading_list[i]

    if book in last_seen:
        next_occurrence[i] = last_seen[book]

    last_seen[book] = i

count_round = 0
max_heap = []
current_next_occ = [inf] * (N + 1)

for i in range(M):
    book = reading_list[i]

    current_next_occ[book] = next_occurrence[i]

    if reading_list[i] not in book_on_table:
        count_round += 1

        if len(book_on_table) >= K:
            while max_heap:
                next_occ, candidate = heappop(max_heap)

                if candidate in book_on_table and next_occ == current_next_occ[candidate]:
                    book_on_table.remove(candidate)
                    break

        book_on_table.add(book)

    heappush(max_heap, (next_occurrence[i], book))

print(count_round)
