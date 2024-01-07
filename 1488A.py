def operation2(x,p):
    return x*(10**p)

for _ in range(int(input())):
    n = input().split()
    x, y = int(n[0]), n[1]
    num = int(y)
    counter = 0
    i = len(y)-1
    while(i >= 0):
        if operation2(x,i) <= num:
            num = num - operation2(x,i)
            counter += 1

        else:
            i -= 1
    print(counter + num)
