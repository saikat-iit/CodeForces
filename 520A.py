n = int(input())
sentence = list(set(list(input().lower())))
if len(sentence) < 26:
    print("NO")
else: print("YES")
