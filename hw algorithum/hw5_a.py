from collections import deque

queue = deque() # คิวที่เก็บเเต่ละโต๊ะจะว่าง 

N = int(input())
exit_time = [0] * N  # เก็บว่ามีคนเข้ามาเเล้วออกตอนไหน
time_now = 0
for i in range(N):
    hour, minute, wait_index = map(int, input().split())
    time_customer = hour * 60 + minute

    while len(queue) != 0 and queue[0] <= time_customer: # เครียร์คิวที่หมดเวลาเเล้ว
        queue.popleft() # ก็คือเอาออกถ้าเสร็จเเล้ว

    if wait_index < len(queue): # Queue is full, customer leaves
        exit_time[i] = time_customer
    else:                       # ถ้าคิวที่เหลืออยู่ > ที่ลูกค้ายอมรอ → ลูกค้าไม่เข้าร้าน บันทึกว่าออกทันทีเวลาที่มาถึง
        if len(queue) == 0: # Queue is empty, customer enters right away
            exit_time[i] = time_customer + 20
            queue.append(time_customer + 20)
        else:              # Queue has people but customer is willing to wait
            exit_time[i] = queue[-1] + 20
            queue.append(queue[-1] + 20)

for i in range(N): # แปลงนาทีกลับเป็น ชั่วโมง นาที แล้ว print
    print(exit_time[i] // 60, exit_time[i] % 60)
