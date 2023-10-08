t = int(input())
for _ in range(t):
    num = input()
    list_num = list(num)
    i1 = list_num.index('1')
    i3 = list_num.index('3')

    if i1 < i3:
        print(13)
    else: print(31)