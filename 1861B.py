# https://codeforces.com/contest/1861/problem/B

def indexs(lst:list, key):
    indexs = []
    for i in range(len(lst)):
        if lst[i] == key:
            indexs.append(i)
    return indexs

t = int(input())
for _ in range(t):
    a = input()
    b = input()