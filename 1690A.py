for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mdiff = max([a[i]-b[i] for i in range(len(a))])
    zmdiff = 0
    result = "YES"
    
    for i in range(len(a)):
        if b[i] != 0:
            if a[i] - b[i] == mdiff:
                continue
            else:
                result = "NO"
                break
        else:
            zmdiff = max(zmdiff, a[i])

    if zmdiff > mdiff & mdiff != 0:
        result = "NO"
                  
    print(result)