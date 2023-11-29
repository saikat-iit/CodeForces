import math
for _ in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    a.sort()
    a[0] = a[0] + 1
    output = math.prod(a)
    print(output)
