for _ in range(int(input())):
    q = int(input())
    arr = list(map(int, input().split()))
    emp = [arr[0], arr[1]]
    
    if q == 1: print("1")
    elif q == 2: print("11")
    else:
        result = '11'
        for i in range(2,q):
            if emp[0] < emp[-1]:
                if arr[i] >= emp[-1] or arr[i] <= emp[0]:
                    emp.append(arr[i])
                    result += "1"
                else: result += "0"

            elif emp[0] == emp[-1]:
                if arr[i] <= emp[-1]:
                    emp.append(arr[i])
                    result += "1"
                else: result += "0"
                
            elif emp[0] > emp[-1]:
                if arr[i] >= emp[-1] and arr[i] <= emp[0]:
                    emp.append(arr[i])
                    result += "1"
                else: result += "0"

        print(result)
