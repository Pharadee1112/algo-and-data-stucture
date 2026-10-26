"""
April in Bangkok is a time of excitement: Songkran, the traditional Thai New Year festival, is just around the corner. Soon, the streets will fill with celebrations and water fights, while families and friends gather to welcome the new year.

A few days before the festival, Niran decided to buy gifts for his relatives and friends. He visited a gift shop’s website to find out how much money he would need.

The website listed all nn items available in the shop, along with the price aiai​ of each item. No two items had the same price. Niran believes that it is the thought that counts, so he decided to buy the kk cheapest distinct items as gifts.

Having chosen the gifts, Niran prepared exactly enough money to buy them at the prices shown on the website and went to the shop.

However, the festive season had a pleasant surprise in store for him: the shop had announced a sale, and the prices of all items had been reduced! Niran learned the new price bibi​ of each item. He now wants to find out how much money he will save by buying the same kk items he originally selected on the website.

Help Niran calculate his total savings: the difference between the original total price of the selected gifts and their total price during the sale.
Input format

The first line of the input file contains two integers nn, kk ( 1≤n≤1051≤n≤105, 1≤k≤n1≤k≤n) — the number of distinct gifts in the shop and the number of people Niran wants to buy gifts for, respectively. The integers are separated by a space.

The second line contains nn distinct integers aiai​ ( 1<ai≤1091<ai​≤109) — the prices of the gifts listed on the shop’s website. The integers are separated by spaces.

The third line contains nn distinct integers bibi​ ( 1≤bi<ai1≤bi​<ai​) — the discounted prices of the gifts. The integers are separated by spaces.
Output format

In the only line of the output file, print the amount of money Niran will save by buying the kk gifts he originally selected.

5 2
5 7 6 9 8
4 1 3 2 7

output : 4
"""

m, k = map(int, input().split())
old_price = list(map(int, input().split()))
new_price = list(map(int, input().split()))
pair = [(old_price[i], new_price[i]) for i in range(m)]
pair.sort()

cost_save = 0

for a, b in pair[:k]:
    cost_save += a - b

print(cost_save)
