for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        for i in range(n,0,-1):
            print(i,end=' ')
        print()
    elif n !=3:
        for i in range(n,n//2+1,-1):
            print(i,end=' ')
        for i in range(1,n//2+2):
            print(i,end=' ')
        print()
    else: print(-1)