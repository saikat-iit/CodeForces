n = int(input())
X = 0
for i in range(n):
    s = input()
    if s == "++X" or s == "X++":
        X = X + 1
    if s == "--X" or s == "X--":
        X = X - 1

print(X)