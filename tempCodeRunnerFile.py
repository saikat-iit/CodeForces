import math
for _ in range(int(input())):
    n = list(map(int, input().split()))
    a, b = n[0], n[1]
    num = 0
    if b%a == 0:
        print(int(b**2/a))
    else:
        print(int(math.lcm(a,b)))