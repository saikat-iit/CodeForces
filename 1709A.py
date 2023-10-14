t = int(input())
for _ in range(t):
    x = int(input())
    keys = list(map(int, input().split()))
    if keys[x-1] == 0:
        print("NO")
    else:
        key = keys[x-1]
        if keys[key-1] == 0:
            print("NO")
        else: print("YES")