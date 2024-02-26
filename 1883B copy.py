from collections import Counter
for _ in range(int(input())):
    n, k = map(int, input().split())
    s, cnt = input(), 0
    lst = list(dict(Counter(s)).values())
    for i in lst:
        if i%2 != 0: cnt += 1
        
    if cnt<=k: print("YES")
    elif cnt-k == 1: print("YES")
    else: print("NO") 