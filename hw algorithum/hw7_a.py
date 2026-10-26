N = int(input())
banknote = list(map(int, input().split()))
S = int(input())

dp = [S + 1] * (S + 1)
dp[0] = 0

for i in range(1, S + 1):
    for note in banknote:
        if i >= note:
            dp[i] = min(dp[i], dp[i - note] + 1)

if dp[S] == S + 1:
    print(-1)
else:
    print(dp[S])


# subproblem : จำนวน min ของ banknote ที่ทำให้ user ได้เงิน i (จำนวนะนบัตรที่รวมกันที่รวมกันน้อยที่สุด ให้ได้d[i])
#         d[:] = -1 เพราะว่าสมมติว่าเรายังให้ไม่ได้ เพราะเราไม่รู้ เพราะถ้าหาไม่ได้ ก็จะให้เป็น -1 ออกมาเ็น output ทันที
# basis : d[0] = 0 เพราะว่าต้องการกดเงิน 0 ก็ไม่ได้ให้อะไร
# induction : d[i] = 