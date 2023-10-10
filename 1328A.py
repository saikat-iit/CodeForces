t = int(input())
for _ in range(t):
    num = list(map(int, input().split()))
    if num[0] % num[1] == 0:
        print(0)
    else:
        print(num[1] - num[0]%num[1])
