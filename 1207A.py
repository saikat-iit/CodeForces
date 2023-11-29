def burger(counter, buns, patty):
    if buns-2 >= 0 and patty-1 >= 0:
        counter += 1
        return counter, buns-2, patty-1, True
    else:
        return counter, buns, patty, False

for _ in range(int(input())):
    # b = buns, p = beef patty, f = chicken cutlet
    quanity = list(map(int, input().split()))
    price = list(map(int, input().split()))
    b, p, f = quanity[0], quanity[1], quanity[2]
    h, c = price[0], price[1]

    h_counter = 0
    c_counter = 0
    profit = 0

    if h >= c:
        check = True
        while check:
            h_counter, b, p, check = burger(h_counter,b,p)
        profit = profit + h*h_counter

        check = True
        while check:
            c_counter, b, f, check = burger(c_counter,b,f)
        profit = profit + c*c_counter
 
    if h < c:
        check = True
        while check:
            c_counter, b, f, check = burger(c_counter,b,f)
        profit = profit + c*c_counter

        check = True
        while check:
            h_counter, b, p, check = burger(h_counter,b,p)
        profit = profit + h*h_counter

    print(profit)
