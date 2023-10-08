import math

def check_sorted(array):
    a_temp_arr = array.copy()
    a_temp_arr.sort()

    if array == a_temp_arr:
        return True
    else:   
        return False

def find_index(array):
    _min = array[-1] - array[-2]
    a, b = 0, 0
    for i in range(len(array)-1):
        if array[i+1] - array[i] <= _min:
            _min = array[i+1] - array[i]
            a, b = i, i+1
    return a, b

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    if check_sorted(array):
        i1, i2 = find_index(array)
        diff = array[i2] - array[i1]

        if diff % 2 == 0:
            print(int(diff/2 + 1))
        else:
            print(math.ceil(diff/2))
    else:
        print(0)