a = list(map(int, list(input())))
b = list(map(int, list(input())))
result = ""

for i in range(len(a)):
    if a[i] == b[i]:
        result += '0'
    else:
        result += '1'

print(result)
