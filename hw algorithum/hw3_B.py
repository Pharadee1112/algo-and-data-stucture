import random

size, weight = map(int, input().split())

total = 0
cost = []

for i in range(size):
    a, b = map(int, input().split())
    if b == 0:
        total += a
    else:
        cost.append([a / b, a, b])


def partition(x, l, r, pivot):
    """
    :param x: Source array (list)
    :param l: left border of partitioning range (int)
    :param r: left border (not included) of partitioning range (int)
    :param pivot: pivot element to divide array (any item from x[l, r)).
    :return: il, ir -- desired partition
    This function should reorder elements of x within [l, r) region
    in the way, these conditions are true:
    x[l:il] < pivot
    x[il:ir] == pivot
    x[ir:r] > pivot
    """
    # Your code goes here
    il = l
    ir = l
    for i in range(l, r):
        if x[i][0] == pivot:
            x[ir], x[i] = x[i], x[ir]
            ir += 1
        elif x[i][0] < pivot:
            x[il], x[i] = x[i], x[il]
            if il < ir:
                x[ir], x[i] = x[i], x[ir]
            il += 1
            ir += 1
    return il, ir


def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)][0]
        il, ir = partition(x, l, r, pivot)
        qsort(x, l, il)
        qsort(x, ir, r)


qsort(cost)

for avg_cost, a, b in cost[::-1]: # ใส่กระเป๋า ที่ตอนนี้เราเรียงมาเเล้วที่มากที่สุด 
    if b <= weight: # เทียบ ถ้าน้ำหนักของของมากกว่าน้ำหนักที่กระเป๋าใส่ได้
        total += a
        weight -= b
    else:
        total += (weight * a) // b # 
        break

print(total)
