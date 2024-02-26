x = list(map(int, input()))
num = ""
if x[0] == 9:
    num = "9"
    for i in range(1,len(x)):
        if x[i] < 5: num += str(x[i])
        else: num += str(9-x[i])
else:
    num = ""
    for i in range(len(x)):
        if x[i] < 5: num += str(x[i])
        else: num += str(9-x[i])
print(num)
