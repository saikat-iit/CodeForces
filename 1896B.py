def operation(n:list):
    if n[1] == max(n):
        return True
    else: return False

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != 1:
        print("NO")
    else:
        i = 1
        while(i<n-1):
            if operation([a[i-1],a[i],a[i+1]]):
                a[i], a[i+1] = a[i+1], a[i]
                i = 1
            else:
                i += 1
                
        b = a.copy()
        b.sort()
        if a == b:
            print("YES")
        else: print("NO")