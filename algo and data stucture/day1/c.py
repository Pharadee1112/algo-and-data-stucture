"""
Alice in Wonderland has nn magic apples. For each apple, it is known that after eating it, her height first decreases by aiai​ centimeters and then increases by bibi​ centimeters. Alice is very hungry and wants to eat all nn apples, but she is afraid that at some moment her height will become zero or less, and she will disappear completely. Help her determine whether it is possible to eat the apples in some order so that at any moment Alice’s height remains greater than zero.
Формат ввода

First line of input contains two integer numbers: nn and ss ( 1≤n≤10001≤n≤1000, 1≤s≤1000001≤s≤100000) — number of apples and initial height of Alice. Each of next nn lines contains pair of integer numbers: aiai​, bibi​, less than 1000.
Формат вывода

If all apples cannot be eaten, print -1, otherwise, print nn numbers — indices of apples in order in which they should be eaten.
"""

"""Idea:
Approach: Greedy + Sorting

1. Split apples into two groups:
   - up:   b >= a (net gain)
   - down: b < a  (net loss)
2. Eat "up" first, sorted by a ascending.
   Why: smallest drop first while height is still low.
3. Then eat "down", sorted by b descending.
   Why: apples that give back the most height go first,
   apples that give back little go last.
4. Before each apple, check height - a > 0, else print -1.

Sort used: Python built-in sort (Timsort), O(n log n), stable.

Complexity:
- Read + split:  O(n)
- Sort:          O(n log n)
- Simulate:      O(n)
- Total time:    O(n log n)
- Memory:        O(n)
"""



size_apple, height = map(int, input().split())

apple = []

for i in range(size_apple):
    a, b = map(int, input().split())
    apple.append([a, b, i + 1])

up = []
down = []

for a, b, idx in apple:
    if b >= a:
        up.append([a, b, idx]) #อันนี้ sort โดยใช้ a โดยจะกิน a = ทำให้เตี้ยที่มีค่าน้อยก่อน a (น้อยไปมาก)
    else:
        down.append([b, a, idx]) #เรีนวความ b โดย กินจาก b ที่ให้ความสูงเยอะก่อน กลุ่มที่ให้ความสูงกลับมามากที่สุด b (มากไปน้อย)

"""ชั้นที่ 1: ทำไมเก็บ [b, a, i] แล้ว sort ได้ตาม b

เพราะ sort() ดู ช่องแรก ก่อนเสมอ
เอา b ไว้ช่องแรก มันก็เรียงตาม b ให้เลย แค่นั้น

ชั้นที่ 2: ทำไมกลุ่ม down ต้องเรียงตาม b มากไปน้อย
ข้อสังเกต 1: ความสูงตอนจบเท่ากันเสมอ

กินลำดับไหนก็ตาม สุดท้ายบวก b ทุกลูก ลบ a ทุกลูกเหมือนกัน
ความสูงตอนจบจึง เท่ากันทุกลำดับ"""

"""Final height is the same in any order. The last apple’s lowest point is (final height - b), 
so the apple with the smallest b should be eaten last. That’s why “down” is sorted by b descending."""


up.sort() #อันนี้คือน้อยไปมากปกติ
down.sort(reverse=True) #reversed

dead = False

for a, b, idx in up:
    if height <= a:
        print(-1)
        dead = True
        break
    height += b - a

if not dead:
    for b, a, idx in down:
        if height <= a:
            print(-1)
            dead = True
            break
        height += b - a

if not dead:
    for i in up:
        print(i[2], end=' ')
    for i in down:
        print(i[2], end=' ')