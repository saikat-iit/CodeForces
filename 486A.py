# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum = sum + ((-1)**i)*i
# print(sum)

## The above code, give time limit exceeded

import math
n = int(input())
if n % 2 == 0:
    print(int(n/2))
else:
    print(-1*math.ceil(n/2))