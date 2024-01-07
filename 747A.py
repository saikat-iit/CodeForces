from functools import reduce
from math import sqrt
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

n = int(input())
f = list(factors(n))
f.sort()
if len(f)%2 == 0:
        print(f[int(len(f)/2-1)],f[int(len(f)/2)])
else:
    print(f[int(len(f)//2)],f[int(len(f)//2)])