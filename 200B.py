n = int(input())
oranges = list(map(int, input().split()))
percent = 0.0
for orange in oranges:
    percent = percent + orange/100

print((percent/(100*n))*100*100)