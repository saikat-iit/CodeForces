k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

counter = 0

if k>d or l>d or m>d or n>d:
    pass
else:
    for i in range(1,d+1):
        if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
            counter += 1
        
print(counter)