n = int(input())
arr = list(map(int, input().split()))
arr_copy = arr.copy()

for i in range(len(arr)-1,0,-1):
    occ = -1
    for j in range(len(arr_copy)):
        if arr_copy[j] == arr[i]:
            occ += 1
    
    for _ in range(occ):
        arr_copy.remove(arr[i])

print(len(arr_copy))
print(*arr_copy, sep=" ")