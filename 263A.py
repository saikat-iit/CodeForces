array = []
for i in range(5):
    array.append(input().split())

r = 0
c = 0
for arr in array:
    if "1" in arr:
        for n in arr:
            if n == "1":
                break
            c = c + 1
        break
    r = r + 1

ans = abs(2-r) + abs(2-c)
print(ans)


