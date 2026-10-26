def sift_up(data, i):
    if i == 0:
        return

    parent = (i - 1) // 2
    if data[parent] > data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def sift_down(data, i):
    child1 = i * 2 + 1
    child2 = i * 2 + 2
    if child1 >= len(data):
        return
    if child2 >= len(data):
        child_min = child1
    else:
        child_min = child1 if data[child1] < data[child2] else child2
    if data[child_min] < data[i]:
        data[i], data[child_min] = data[child_min], data[i]
        sift_down(data, child_min)


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


n = list(map(int, input().split()))
heapify(n)

tax = 0

while len(n) > 1:
    new_enterprise = heappop(n) + heappop(n)
    tax += new_enterprise * 0.05
    heappush(n, new_enterprise)

print(f"{tax: .10f}")
