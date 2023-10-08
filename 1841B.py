def sorted(arr:list):
    s_arr = arr.copy()
    s_arr.sort()
    if s_arr == arr: return True
    else: return False

def beautiful(arr):
    check = True
    for i in range(len(arr)):
        copy_arr = arr.copy()
        temp = []
        for j in range(i+1):
            temp.append(arr[j])
        for i in temp:
            copy_arr.remove(i)
            copy_arr.append(i)
        if sorted(copy_arr):
            check = True
    return check
    
t = int(input())
for _ in range(t): 
    q = int(input())
    arr = list(map(int, input().split()))
    a = []
    result = ''
    for i in range(len(arr)):
        a.append(arr[i])
        if beautiful(a):
            result += '1'
        else:
            result += '0'
            a.pop()

    print(result)