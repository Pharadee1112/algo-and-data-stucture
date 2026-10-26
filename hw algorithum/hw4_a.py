# MIPT teachers continue to analyse results of this year courses. And again, they can’t do without your help!

# This time number of students was 0≤N≤1000000≤N≤100000, and teachers want to check if courses were too easy or too difficult. To do that they need to check number of students whose average score is within given range: l≤score≤rl≤score≤r.

# Please, help the teachers and write the program which can process such requests fast. The number of requests teachers prepared for you is 0≤M≤1000000≤M≤100000.
# Input format

# First line contains two integer numbers divided by space character: 0≤N,M≤1000000≤N,M≤100000 — number of students and requests respectively. Second line contains NN numbers divided by space character: scores of students. 0≤si≤1090≤si​≤109. Each of the following M lines contains two integer numbers: lj,rjlj​,rj​, divided by space character: 0≤lj≤rj≤1090≤lj​≤rj​≤109
# Output format

# For each request (lj,rj)(lj​,rj​) print one integer number on separate line: number of students who got score within requested range: ∣∣{i:lj≤si≤rj}∣∣∣{i:lj​≤si​≤rj​}∣.
# Sample 1
# Input
# 6 6
# 1 1 2 2 2 3
# 1 1
# 2 2
# 3 3
# 1 2
# 2 3
# 1 3

# Output
# 2
# 3
# 1
# 5
# 4
# 6

def bsearch_l(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def bsearch_r(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


N, M = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()

character = []
for i in range(M):
    character.append(list(map(int, input().split())))
    
for mn, mx in character:
    left = bsearch_l(scores, mn)
    right = bsearch_r(scores, mx)
    print(right - left)
