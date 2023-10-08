n = int(input())
result = list(input())
A = result.count('A')
D = result.count('D')
if A > D:
    print('Anton')
elif A < D:
    print('Danik')
else: print('Friendship')