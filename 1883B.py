from collections import Counter

def odd(i:int):
    if i%2 == 0: return False
    else: return True

def cnt_odd(lst:list):
    cnt = 0
    for i in lst:
        if odd(i): cnt += 1
    return cnt

def palindrome(lst:str):
    cnt = cnt_odd(lst)
        
    if cnt > 1: return False
    else: return True

for _ in range(int(input())):
    t = list(map(int, input().split()))
    n, k = t[0], t[1]
    s = input()
    dict_s = dict(Counter(s))
    lst_value = list(dict_s.values())
    check = True

    while(check):
        if k == 0 or cnt_odd(lst_value) == 0:
            check = False
        
        for i in range(len(lst_value)):
            if odd(lst_value[i]) and k > 0:
                lst_value[i] -= 1
                k -= 1
            if k == 0:
                break
  
    dict_s = dict(zip(list(dict_s.keys()), lst_value))

    if k>1:
        check = True
        while(check):
            if k == 0 or k == 1:
                check = False
            
            for i in range(len(lst_value)):
                if k > 0:
                    if lst_value[i] - 2 >= 0: lst_value[i] -= 2
                    if k - 2 >= 0: k -= 2
                if k == 0 or k == 1:
                    break

    dict_s = dict(zip(list(dict_s.keys()), lst_value))
    
    if palindrome(list(dict_s.values())) and k == 1:
        print("YES")
    elif palindrome(list(dict_s.values())) and k == 0:
        print("YES")
    else: print("NO")