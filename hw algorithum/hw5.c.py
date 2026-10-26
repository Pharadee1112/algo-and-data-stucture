from collections import deque


def balance(shop, store):
    if len(shop[store][0]) < len(shop[store][1]):
        shop[store][0].append(shop[store][1].popleft())
    elif len(shop[store][0]) > len(shop[store][1]) + 1:
        shop[store][1].appendleft(shop[store][0].pop())


N = int(input())
shop = [[deque(), deque()] for _ in range(N)]

while True:
    s = input().split()
    if s[0] == "#":
        break
    operation = s[0]
    store = int(s[1])

    if operation == "+":
        customer_id = int(s[2])
        shop[store][1].append(customer_id)
        balance(shop, store)
    elif operation == "!":
        customer_id = int(s[2])
        shop[store][1].appendleft(customer_id)
        balance(shop, store)
    elif operation == "-":
        print(shop[store][0].popleft())
        balance(shop, store)
    elif operation == "?":
        print(len(shop[store][0]) + len(shop[store][1]))
