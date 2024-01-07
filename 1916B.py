import math
for _ in range(int(input())):
    n = list(map(int, input().split()))
    a, b = n[0], n[1]
    num = 0
    if b%a == 0:
        print(int(b*b/a))
    else:
        print(int(a*b/math.gcd(a,b))) #LCM is not avai