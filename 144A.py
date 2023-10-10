n = int(input())
soldiers = list(map(int, input().split()))
index_max = soldiers.index(max(soldiers))
index_min = len(soldiers) - 1 - soldiers[::-1].index(min(soldiers))

if index_min < index_max:
    print(index_max + (len(soldiers) - 1) - index_min - 1)
else:
    print(index_max + (len(soldiers) - 1) - index_min)