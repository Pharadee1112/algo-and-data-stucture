size = int(input())

id_score_name = []

for i in range(size):
    temp = input().split() # collect it in tuple
    id_score_name.append((int(temp[0]), int(temp[1]), temp[2])) # เก็บเป็น list เเล้วแปลงเป็น int int str

for i in range(size - 1): # arrange ID by Selection Sort 
    min_id = i
    for j in range(i + 1, size):
        if id_score_name[j][0] < id_score_name[min_id][0]:
            min_id = j
    id_score_name[i], id_score_name[min_id] = id_score_name[min_id], id_score_name[i]

for i in range(1, size): #arrange score by insertion sort เพราะว่ามันข้ามค่าที่มีค่าเท่ากันไป ทำไมลำดับเดิม ที่เรียงกัน เป็นเหมือนเดิมอยู่
    key = id_score_name[i]
    j = i - 1
    while j >= 0 and key[1] > id_score_name[j][1]:
        id_score_name[j + 1] = id_score_name[j]
        j -= 1
    id_score_name[j + 1] = key

for i in range(3): # print name that index two, students who took 1st, 2nd and 3rd place in sorted table
    print(id_score_name[i][2])

for i in range(size): # print student id that sort in the same line
    print(id_score_name[i][0], end=' ')
