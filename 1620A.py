for _ in range(int(input())):
    s = list(input())
    count = 0
    for i in s:
        if i == "N":
            count += 1
    
    if count == 1:
        print("NO")

    else: print("YES")