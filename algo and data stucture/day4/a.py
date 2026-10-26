original = input()
shifted = input()

if len(original) != len(shifted):
    print("-1")
else:
    n = len(original)
    s = shifted * shifted
    ans = s.find(original)

    print(ans)


