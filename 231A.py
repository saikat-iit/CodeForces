n = int(input())
count = 0
if n >=1 and n <= 1000:
    for i in range(n):
        s = input().split()
        sum = 0
        for i in list(s):
            sum = sum + int(i)
        if sum >= 2:
            count = count + 1

print(count)
