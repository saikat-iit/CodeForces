n = list(input())
counter = 0
for i in range(len(n)-1):
    if n[i+1] == n[i]:
        counter += 1
        if counter == 6: break
    else: counter = 0

if counter >= 6: print("YES")
else: print("NO")