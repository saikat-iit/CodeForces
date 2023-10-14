for _ in range(int(input())):
    coins = list(map(int, input().split()))
    a, b, c, n = coins[0], coins[1], coins[2], coins[3]
    t = (n -(2*b - (a + c)))/3
    x, y, z = (b-a) + t, t, (b-c) + t

    if t.is_integer() and x>=0 and y>=0 and z>=0:
        print("YES")
    else: print("NO")
