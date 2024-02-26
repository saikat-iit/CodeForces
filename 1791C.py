for _ in range(int(input())):
    n = input()
    s = list(input())
    t = s.copy()
    t.reverse()
    count = 0
    for i in range(0,int(len(s)/2)):
        if s[i] != t[i]:
            count += 2
        else: break
    print(len(s) - count)