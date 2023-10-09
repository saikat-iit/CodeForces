n = int(input())
p = list(map(int, input().split()))
init_arr = []

for _ in p:
    init_arr.append(0)

for i in range(len(p)):
    init_arr[p[i]-1] = i+1

print(*init_arr)