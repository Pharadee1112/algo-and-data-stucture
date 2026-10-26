size_apple, height = map(int, input().split()) # get data = แอปเปิลมีกี่ลูก กับความสูงเริ่มต้น

apple = []

for i in range(size_apple): # เก็บเป็น list 
    a, b = map(int, input().split()) # ให้ตัวเลขที่เข้ามา 2 ตัวนั้นมันคือ tuple เเล้วเปลี่ยนเป็น int
    apple.append([a, b, i + 1]) # เเล้วเก็บเข้าที่ apple = []

good = []
bad = []

for a, b, idx in apple: # sorting the apple goog or bad
    if b >= a: # เพราะว่าถ้า b มากกว่า a ก็คือเรากินเข้าไปเเล้วจะได้ net.height
        good.append([a, b, idx])
    else: # a > b = bad
        bad.append([a, b, idx])

for i in range(len(good) - 1): # sorting good apple first by using selection sorting
    min_a = i 
    for j in range(i + 1, len(good)): 
        if good[j][0] < good[min_a][0]:
            min_a = j
    good[i], good[min_a] = good[min_a], good[i]

for i in range(len(bad) - 1): # sorting bad apple by using selecion sorting
    max_b = i
    for j in range(i + 1, len(bad)):
        if bad[j][1] > bad[max_b][1]:
            max_b = j
    bad[i], bad[max_b] = bad[max_b], bad[i]

dead = False # วนก่อน ให้ระบบ false ไปก่อน

for a, b, idx in good: # check ว่ากินเเล้วตายไหม print -1 เเล้วระบบไม่เดินต่อ ก็ break
    if height <= a:
        print(-1)
        dead = True
        break
    height += b - a

if not dead: # check ถ้าไม่ตาย 
    for a, b, idx in bad:
        if height <= a: # เช็กว่า
            print(-1)
            dead = True
            break
        height += b - a

if not dead: # ถ้าไม่ตาย print 
    for i in good:
        print(i[2], end=' ')

    for i in bad:
        print(i[2], end=' ')
