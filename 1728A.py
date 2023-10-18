for _ in range(int(input())):
    n = int(input())
    cnts = list(map(int, input().split()))
    print(cnts.index(max(cnts))+1)