import itertools

def GET(lst:list,n:int):
    sums = []
    for i in range(1,len(lst)+1):
        ss = list(map(list, itertools.combinations(lst, i)))
        for j in range(len(ss)):
            sums.append(sum(ss[j]))
    if n in sums: return 1
    else: return 0

ms = []
for m in range(int(input())):
    result = ''
    t, v = map(int, input().split())
    if t == 1: ms.append(2**v)
    else:
        if GET(ms,v): print("YES")
        else: print("NO")