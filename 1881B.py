from collections import Counter

def equality(lst:list):
    if len(Counter(lst)) == 1:
        return True
    else: return False

for _ in range(int(input())):
    n = list(map(int, input().split()))
    if equality(n): print("YES")
    else:
        for i in range(3):
            n.sort()
            _min = n[0]
            _max = n[-1]
            m1, m2 = _min, _max -_min
            n.pop()
            n.append(m1)
            n.append(m2)
            if equality(n):
                print("YES")
                break
            elif i == 2:
                print("NO")
            else:
                continue
