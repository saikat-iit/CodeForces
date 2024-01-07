for _ in range(int(input())):
    n = int(input())
    if n%3==2:
        x = int((n+4)/3)
        print(x-1,x,x-3)
    if n%3==1:
        x = int((n+5)/3)
        print(x-2,x,x-3)
    if n%3==0:
        x = int((n+3)/3)
        print(x-1,x,x-2)
