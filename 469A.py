# n = int(input())
# p = list(set(list(map(int, input().split()))))
# q = list(set(list(map(int, input().split()))))

# levels = [i+1 for i in range(n)]
# levels_pass = list(set(p+q))
# try:
#     levels_pass.remove(0)
# except Exception as e: pass
# levels_pass.sort()


# if levels_pass == levels: print("I become the guy.")
# else: print("Oh, my keyboard!")

level =  set(range(1, int(input()) + 1))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = set(x[1:])
y = set(y[1:])

print('I become the guy.' if level - (x | y) == set() else 'Oh, my keyboard!')